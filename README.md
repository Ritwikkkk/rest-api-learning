# rest-api-learning
This repo will be consisting of basic codes about how to use Rest APIs in python.

🔹 1. What is a REST API?

A REST API is a way for two systems to communicate over the internet using HTTP.
It exposes resources via endpoints like /predict or /health, allowing clients to send data and receive responses, usually in JSON.

🔹 2. Why do Data Scientists need REST APIs?

Because REST APIs allow you to:

Deploy ML models for real-time inference

Integrate models into apps, dashboards, and agents

Build microservices

Provide predictions to external clients

REST APIs turn your model into a service.

🔹 3. What are common HTTP methods?
Method	Use Case
GET	Fetch information (no request body)
POST	Send data for processing (model inference)
PUT	Update existing data
DELETE	Remove data

Data Scientists mainly use GET and POST.

🔹 4. What is an endpoint?

A URL path that performs an action.

Examples:

/predict

/health

/upload

🔹 5. Difference between GET and POST?
GET:

Used to retrieve data

No request body

Parameters go in URL

Safe and idempotent

POST:

Used to send data

Request body usually JSON

Used for actions like model prediction

🔹 6. Why is POST used for predictions?

Prediction requires sending a JSON payload (text, features, image, etc.).
POST is designed for sending data safely.

🔹 7. Simple example of a Flask POST endpoint
@app.post("/predict")
def predict():
    data = request.get_json()
    prediction = model.predict(data["text"])
    return jsonify({"prediction": prediction})

🔹 8. Why do browsers show 404 or 405 when you hit /predict directly?

Browser sends GET requests

/predict expects POST

Therefore you get 405 Method Not Allowed

🔹 9. What is FastAPI? Why is it better for ML?

FastAPI advantages:

Automatic documentation (/docs)

Built-in validation with Pydantic

Faster performance

Uses async for high throughput

Cleaner syntax

Perfect for ML/DS microservices.

🔹 10. Example of a FastAPI POST endpoint
@app.post("/predict")
def predict(request: PredictRequest):
    return {"prediction": model(request.text)}

🔹 11. What is Pydantic?

A data validation library used in FastAPI.

Advantages:

Validates request body automatically

Ensures correct types

Avoids manual checks

Example:

class PredictRequest(BaseModel):
    text: str

🔹 12. How to test FastAPI endpoints?

Multiple ways:

Swagger UI → /docs

Postman

curl

Python requests library

🔹 13. Why do we need API keys?

To secure your API so that only authorized users can access it.

Prevents:

Abuse

Overuse

Unauthorized usage

🔹 14. How does API key authentication work?

Client sends:

x-api-key: YOUR_KEY


Server checks:

If key matches → allow

Else → return 401 Unauthorized
