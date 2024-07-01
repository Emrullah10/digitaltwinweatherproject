from flask import Flask, request, jsonify
from flask_cors import CORS
from AI.ModelAI import power_predicted

app = Flask(__name__)
CORS(app)  # CORS hatasını önlemek için gerekli

predictor = power_predicted()


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    temperature_values = data.get("temperature", [])

    # "temperature_values" bir liste mi ve en az bir eleman içeriyor mu kontrol etme
    if not isinstance(temperature_values, list) or len(temperature_values) == 0:
        return jsonify({"error": "Temperature values should be a non-empty list."}), 400

    # Tahminleri yapmak için sıcaklık değerlerini kullan
    predicted_powers = [predictor.predict_power(temperature) for temperature in temperature_values]

    return jsonify({"predicted_powers": predicted_powers})


if __name__ == '__main__':
    app.run(debug=True)
