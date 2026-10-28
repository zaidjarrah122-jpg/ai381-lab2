AI381 Lab 2 - Automated ML Delivery Pipeline









Project Overview



A customer churn prediction API built with FastAPI and scikit-learn. This project demonstrates automated testing, containerization, vulnerability scanning, and Docker image publishing through GitHub Actions.



Features

FastAPI prediction API

Input validation with Pydantic

Health-check endpoint

Automated tests with pytest

Multi-stage Docker build

Non-root container execution

Trivy vulnerability scanning

Automated publishing to GitHub Container Registry (GHCR)

Run with One Command



Make sure Docker is installed and running, then execute:



docker run --rm -p 8000:8000 ghcr.io/zaidjarrah122-jpg/ai381-lab2:913f96c9a98efa832fbded7acbb1ae78e9fd3f73

API Endpoints

Health Check



GET /health



Example response:



{

&#x20; "status": "ok"

}

Predict Customer Churn



POST /predict



Example request:



{

&#x20; "tenure\_months": 12,

&#x20; "monthly\_fee": 75.0,

&#x20; "contract": "Month-to-month",

&#x20; "internet\_service": "Fiber optic",

&#x20; "support\_calls": 2

}



Example response:



{

&#x20; "churn\_probability": 0.316

}



The probability shown is an example. The actual result depends on the model and input.



Interactive API documentation is available at http://localhost:8000/docs while the container is running.



Run Tests Locally



Using Python 3.12 and the project dependencies:



python -m pytest -v

Docker Image



Registry: GitHub Container Registry (GHCR)



Image:



ghcr.io/zaidjarrah122-jpg/ai381-lab2:913f96c9a98efa832fbded7acbb1ae78e9fd3f73



Image Digest:



sha256:20f33e6709e2d25fce3ad4fbf841bd848fd5f3cda86fc60704f8da12020d92c2



Continuous Integration



GitHub Actions runs the test workflow on pushes to main and pull requests targeting main. The Docker workflow builds the image, scans it with Trivy, and publishes it to GHCR on pushes to main.



Repository



https://github.com/zaidjarrah122-jpg/ai381-lab2

