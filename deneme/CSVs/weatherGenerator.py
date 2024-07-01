import requests
import pandas as pd
from datetime import datetime

# OpenWeatherMap API anahtarınızı buraya ekleyin
api_key = '19d984c8fec2386543dbedd03c46f65c'
cities = ['Ankara', 'Antalya', 'Erzurum', 'Izmir', 'Burdur', 'Bursa']

# Şehirlerin sayısal değerlerini belirleme
city_mapping = {city: i for i, city in enumerate(cities)}

# Hava durumu açıklamalarını sayısal değerlere dönüştürmek için bir sözlük
weather_mapping = {
    'clear sky': 0,
    'few clouds': 1,
    'scattered clouds': 2,
    'broken clouds': 3,
    'shower rain': 4,
    'rain': 5,
    'thunderstorm': 6,
    'snow': 7,
    'mist': 8
}

# Boş bir DataFrame oluşturma
weather_data = []

for city in cities:
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    # Verileri kontrol etme
    if 'main' in data and 'weather' in data and 'wind' in data:
        # Saat bilgisini alarak sadece saat kısmını alın
        timestamp = datetime.fromtimestamp(data['dt'])
        hour = timestamp.hour

        # Hava durumu açıklamasını sayısal değere dönüştürme
        weather_description = data['weather'][0]['description']
        weather_numeric = weather_mapping.get(weather_description, -1)  # Bilinmeyen durumlar için -1

        # Gerekli verileri alma
        weather = {
            'City': city_mapping[city],  # Şehirlerin sayısal değerini kullanma
            'Time': hour,
            'Temperature': data['main']['temp'],
            'Weather': weather_numeric,
            'Humidity': data['main']['humidity'],
            'Wind Speed': data['wind']['speed']
        }

        weather_data.append(weather)
    else:
        print(f"Hava durumu verileri alınamadı: {city}")

# DataFrame oluşturma
df = pd.DataFrame(weather_data)

# Verileri CSV dosyasına kaydetme
df.to_csv('weather_data_with_hour.csv', index=False)

print("Hava durumu verileri 'weather_data_with_hour.csv' dosyasına başarıyla kaydedildi.")
