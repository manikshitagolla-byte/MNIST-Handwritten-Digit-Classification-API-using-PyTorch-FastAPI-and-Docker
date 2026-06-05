# MNIST Handwritten Digit Classification API

## Project Overview
This project implements a handwritten digit classification system using PyTorch and FastAPI. The model is trained on the MNIST dataset and deployed through a REST API.

## Features
- Handwritten digit classification
- Deep Learning model using PyTorch
- FastAPI-based REST API
- Model saving and loading
- Docker support
- Interactive API documentation with Swagger UI

## Technologies Used
- Python 3.11
- PyTorch
- FastAPI
- Uvicorn
- Docker

## Project Structure

project/
├── Dockerfile
├── LICENSE
├── README.md
├── app.py
├── doc.1.png
├── doc.2.png
├── fastAPI.png
├── http127.0.0.18000predict.png
├── interference.py
├── mnist_model.pth
├── requirements.txt
├── train.py
└── training complete.png

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Train the Model

```bash
py -3.11 train.py
```

This will:
- Download the MNIST dataset
- Train the neural network
- Save the model as `mnist_model.pth`

## Run the API

```bash
py -3.11 -m uvicorn app:app --reload
```

Server will start at:

```text
http://127.0.0.1:8000
```

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Home Endpoint

```http
GET /
```

Response:

```json
{
  "message": "API is working"
}
```

### Prediction Endpoint

```http
GET /predict
```

Response:

```json
{
  "predicted_digit": 7
}
```

## Docker

Build Docker image:

```bash
docker build -t mnist-api .
```

Run Docker container:

```bash
docker run -p 8000:8000 mnist-api
```

## Output

- Trained model file: `mnist_model.pth`
- FastAPI documentation: `/docs`
- Prediction endpoint: `/predict`

## Author

Golla Manikshita

## License

MIT License
