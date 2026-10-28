from pathlib import Path

import joblib
from fastapi.testclient import TestClient

from src.app.main import app


client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_model_loads():
    model_path = Path(__file__).resolve().parents[1] / "model.joblib"

    assert model_path.exists()

    loaded_model = joblib.load(model_path)

    assert hasattr(loaded_model, "predict_proba")
    assert loaded_model.n_features_in_ == 5


def test_predict_returns_probability():
    customer = {
        "tenure_months": 12,
        "monthly_fee": 50.0,
        "contract": "Month-to-month",
        "internet_service": "Fiber optic",
        "support_calls": 2,
    }

    response = client.post("/predict", json=customer)

    assert response.status_code == 200

    result = response.json()

    assert "churn_probability" in result
    assert 0 <= result["churn_probability"] <= 1


def test_predict_rejects_missing_field():
    customer = {
        "tenure_months": 12,
        "monthly_fee": 50.0,
        "contract": "Month-to-month",
        "internet_service": "Fiber optic",
    }

    response = client.post("/predict", json=customer)

    assert response.status_code == 422


def test_prediction_is_deterministic():
    customer = {
        "tenure_months": 12,
        "monthly_fee": 50.0,
        "contract": "Month-to-month",
        "internet_service": "Fiber optic",
        "support_calls": 2,
    }

    first = client.post("/predict", json=customer)
    second = client.post("/predict", json=customer)

    assert first.status_code == 200
    assert second.status_code == 200

    assert (
        first.json()["churn_probability"]
        == second.json()["churn_probability"]
    )