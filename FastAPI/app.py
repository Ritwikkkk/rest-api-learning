from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader

app = FastAPI()


# 🔑 Define API key
API_KEY = "my-secret-key-123"   # store in ENV in real apps
API_KEY_NAME = "x-api-key"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

# 🔐 Auth dependency
def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key"
        )
    return api_key


class InputData(BaseModel):
    text: str


def dummy_model(text):
    return len(text)


@app.get("/health", dependencies=[Depends(verify_api_key)])
def health_check():
    return {
        "status": "healthy",
        "status_code": 200
        }

@app.post("/predict", dependencies=[Depends(verify_api_key)])
def predict(input_data: InputData):
    prediction = dummy_model(input_data.text)
    return {
        "Input": input_data.text,
        "Prediction": f"The string length of '{input_data.text}' is: {prediction}"
    }

