from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "API is working"}


@app.get("/predict")
def predict():
    return {"predicted_digit": 7}
