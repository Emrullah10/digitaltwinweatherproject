from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# OpenWeatherMap API anahtarınızı buraya ekleyin
API_KEY = '19d984c8fec2386543dbedd03c46f65c'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = 'Antalya'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=tr'

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': data['wind']['speed']
        }
        return jsonify(weather_data)
    else:
        return jsonify({'error': 'Hava durumu bilgisi alınamadı.'}), response.status_code

if __name__ == '__main__':
    app.run(port=5005)