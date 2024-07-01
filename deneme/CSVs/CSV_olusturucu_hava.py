import pandas as pd
import requests

# Örnek şehirler ve API anahtarı
cities = ['Antalya', 'Ankara', 'Izmir', 'Erzurum', 'Burdur', 'Bursa']
api_key = '19d984c8fec2386543dbedd03c46f65c'

# Şehirleri sayısal forma dönüştürme
city_mapping = {city: i for i, city in enumerate(cities)}

# Hava durumu verilerini çeken fonksiyon
def get_weather_data(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_data = {
            'City': city_mapping[city],  # Şehir ismini sayısal değere dönüştürme
            'Temperature': data['main']['temp'],
            'Weather': data['weather'][0]['main'],  # Hava durumu açıklamasını alıyoruz
            'Humidity': data['main']['humidity'],
            'Pressure': data['main']['pressure'],
            'Wind Speed': data['wind']['speed']
        }
        return weather_data
    else:
        print(f"Error fetching data for {city}: {data.get('message', 'Unknown error')}")
        return None

# Şehirlerin hava durumu verilerini çekme ve CSV'ye kaydetme
for city in cities:
    weather_data = get_weather_data(city, api_key)

    if weather_data:
        # Hava durumu açıklamasını sayısal değere dönüştürme
        if weather_data['Weather'] == 'Clear':
            weather_data['Weather'] = 0
        elif weather_data['Weather'] == 'Clouds':
            weather_data['Weather'] = 1
        elif weather_data['Weather'] == 'Rain':
            weather_data['Weather'] = 2
        elif weather_data['Weather'] == 'Snow':
            weather_data['Weather'] = 3
        else:
            weather_data['Weather'] = 4  # Diğer durumlar için

        # DataFrame oluşturma
        df = pd.DataFrame([weather_data])

        # CSV dosyasına kaydetme
        csv_filename = f'{city}_weather.csv'
        df.to_csv(csv_filename, index=False)

        print(f"{city} için hava durumu verileri '{csv_filename}' dosyasına kaydedildi.")