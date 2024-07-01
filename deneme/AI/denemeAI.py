import pandas as pd
import numpy as np
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.impute import SimpleImputer

# CSV dosyasını yükleme
file_path = r'C:\Users\ibrah\OneDrive\Desktop\deneme\CombinedCSV\combined_data.csv'
data = pd.read_csv(file_path)

# Gerekli sütunlar
required_columns = ['Power (W)', 'Temperature', 'Humidity', 'Pressure', 'Wind Speed', 'Time']

# Eksik sütunları kontrol etme ve eklenmesi gereken sütunları ekleme
for column in required_columns:
    if column not in data.columns:
        data[column] = np.nan

# Eksik sütunları geçici olarak doldurmak için NaN olmayan bir değer ekleme
for column in required_columns:
    if data[column].isna().all():
        data.loc[0, column] = 0  # Bu değer sonrasında doldurulacak

# Eksik değerleri ortalama ile doldurma
imputer = SimpleImputer(strategy='mean')
data[required_columns] = imputer.fit_transform(data[required_columns])

# Eksik sütunları orijinal olarak doldurmak için NaN değerleri geri ekleme
for column in required_columns:
    if data.loc[0, column] == 0 and data[column].isna().all():
        data[column] = np.nan

# Bağımsız değişkenler (X) ve bağımlı değişken (y) ayrıştırma
X = data[['Power (W)', 'Temperature', 'Humidity', 'Pressure', 'Wind Speed']]
y = data['Time']  # Zaman sütunu

# Eğitim ve test veri setlerini oluşturma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# SVM modelini oluşturma ve eğitme
svm_model = SVR(kernel='rbf')
svm_model.fit(X_train, y_train)

# Eğitim ve test veri setlerini kullanarak modelin performansını değerlendirme
y_train_pred = svm_model.predict(X_train)
y_test_pred = svm_model.predict(X_test)

# R2 skoru (modelin açıklama gücü) hesaplama
train_r2_score = r2_score(y_train, y_train_pred)
test_r2_score = r2_score(y_test, y_test_pred)

# Ortalama karesel hata (MSE) hesaplama
train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)

# Model performansını yazdırma
print("SVM Eğitim R2 Skoru:", train_r2_score)
print("SVM Test R2 Skoru:", test_r2_score)
print("SVM Eğitim MSE:", train_mse)
print("SVM Test MSE:", test_mse)

# Zaman aralığını tahmin eden fonksiyon
def predict_time_interval(row):
    input_data = pd.DataFrame([row],
                              columns=['Power (W)', 'Temperature', 'Humidity', 'Pressure', 'Wind Speed'])
    time_prediction = svm_model.predict(input_data)
    return time_prediction[0]

# İlk 6 satırın verilerine göre zaman aralığı tahmini yapma ve yazdırma
for i in range(6):
    row = data.iloc[i][['Power (W)', 'Temperature', 'Humidity', 'Pressure', 'Wind Speed']]
    predicted_time_interval = predict_time_interval(row)
    print(f"{i+1}. satırın verileri:", row.to_dict())
    print(f"Tahmin edilen zaman aralığı (Time):", predicted_time_interval)
