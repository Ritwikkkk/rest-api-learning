from flask import Flask, request, jsonify

app = Flask(__name__)

def get_length(text):
    return len(text)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400
    text = data["text"]
    prediction = get_length(text)
    return jsonify({"message": f"The string length of '{text}' is: " + str(prediction)}), 200

@app.route('/puch', methods=['POST'])
def publish():
    return jsonify({"message": "Puchicat ekta beral, boro beral"}), 200

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/model-info', methods=['GET'])
def model_info():
    return jsonify({
        "model": "XGBoost",
        "version": "1.0.0",
        "description": "This is a model for predicting the length of a text",
        "author": "John Doe",
        "email": "john.doe@example.com",
        "website": "https://www.example.com",
        "license": "MIT",
        "license_url": "https://www.example.com/license",
    }), 200


@app.route('/', methods=['GET'])
def home():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)