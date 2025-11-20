# Excel/CSV Converter

A minimal FastAPI application for converting Excel files to CSV and CSV files to Excel.

## Features

- Convert Excel (.xlsx) to CSV
- Convert CSV to Excel (.xlsx)
- Simple web interface
- Docker & Docker Compose ready
- Kubernetes manifests included
- CI/CD with GitHub Actions

## Quick Start

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

3. Open your browser at http://localhost:8000

### Docker

Build and run with Docker:
```bash
docker build -t excel-csv-converter .
docker run -p 8000:8000 excel-csv-converter
```

### Docker Compose

```bash
docker-compose up
```

### Kubernetes (Minikube)

1. Start Minikube:
```bash
minikube start
```

2. Build and load image:
```bash
docker build -t excel-csv-converter:latest .
minikube image load excel-csv-converter:latest
```

3. Deploy:
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

4. Access the application:
```bash
minikube service excel-csv-converter
```

The service will be available at NodePort 30080.

## GitHub Actions Setup

Add these secrets to your GitHub repository:
- `DOCKER_USERNAME`: Your Docker Hub username
- `DOCKER_PASSWORD`: Your Docker Hub password or access token

The workflow will automatically:
- Build the Docker image on push to main
- Tag with `latest` and commit SHA
- Push to Docker Hub

## API Endpoints

- `POST /excel-to-csv`: Upload Excel file, get CSV
- `POST /csv-to-excel`: Upload CSV file, get Excel
- `GET /`: Redirect to web interface

## Project Structure

```
/
├── main.py                  # FastAPI application
├── requirements.txt         # Python dependencies
├── Dockerfile              # Docker image configuration
├── docker-compose.yml      # Docker Compose configuration
├── static/
│   └── index.html          # Web interface
├── k8s/
│   ├── deployment.yaml     # Kubernetes Deployment
│   └── service.yaml        # Kubernetes Service
└── .github/workflows/
    └── deploy.yml          # CI/CD pipeline
```

## Technologies

- **Backend**: FastAPI + Pandas + OpenPyXL
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **CI/CD**: GitHub Actions
