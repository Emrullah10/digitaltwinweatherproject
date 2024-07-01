import pandas as pd

# Şehirlerin hava durumu CSV dosyaları
weather_files = [
    r'C:\Users\ibrah\OneDrive\Desktop\deneme\Databases\weather_data_with_hour.csv',
    ]

# Raspberry Pi ve güneş paneli CSV dosyaları
additional_files = [
    r'C:\Users\ibrah\OneDrive\Desktop\rasberrypi_csv\grouped_raspberry_pi_datasheet_random_data.csv',
    r'C:\Users\ibrah\OneDrive\Desktop\solarpanel_csv\random_data.csv'
]

# Tüm dosyaların listesi
all_files = weather_files + additional_files

# Boş bir DataFrame oluşturma
combined_df = pd.DataFrame()

# Tüm dosyaları tek bir DataFrame'de yan yana birleştirme
for file in all_files:
    df = pd.read_csv(file)
    combined_df = pd.concat([combined_df, df], axis=1)

# Birleştirilen verileri yeni bir CSV dosyasına kaydetme
combined_df.to_csv('combined_data.csv', index=False)

print("Tüm veriler 'combined_data.csv' dosyasına başarıyla birleştirildi.")