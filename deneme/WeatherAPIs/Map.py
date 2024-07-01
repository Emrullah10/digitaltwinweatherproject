import gmplot

# API anahtarınızı buraya ekleyin
api_key = 'AIzaSyCSbfGTTLKs_G6bch67J61SwGa-fuGyWes'

# Türkiye'nin koordinatları (Türkiye'nin merkezi yakınları)
latitude = 39.3334
longitude = 34.8597

# Harita oluşturma
gmap = gmplot.GoogleMapPlotter(latitude, longitude, 7, apikey=api_key)

# Haritayı kaydetme
gmap.draw("C:/Users/ibrah/OneDrive/Desktop/deneme/Map_Files/turkey_map.html")

print("Harita 'turkey_map.html' dosyasına kaydedildi. Tarayıcıda açarak haritayı görüntüleyebilirsiniz.")
