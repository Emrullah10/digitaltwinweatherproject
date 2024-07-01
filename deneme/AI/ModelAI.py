import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score

# Veriyi yükleme
file_path = r'C:\Users\ibrah\OneDrive\Desktop\deneme\GenerateCSV\combined_data.csv'
data = pd.read_csv(file_path)

# Her sütundaki NaN değerlerin sayısını kontrol etme
nan_counts = data.isna().sum()
print("Her sütundaki NaN değerlerin sayısı:")
print(nan_counts)

# NaN değerleri ortalama ile doldurma
data = data.fillna(data.mean())

# Bağımsız değişkenler (X) ve bağımlı değişken (y) ayrıştırma
X = data.drop(columns=['Power (W)'])
y = data['Power (W)']

# X ve y veri setlerinin boyutlarını inceleme
print(X.shape)
print(y.shape)

# Eğitim ve test veri setlerini oluşturma
try:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print("Eğitim ve test veri setleri başarıyla oluşturuldu.")
except ValueError as e:
    print("Eğitim ve test veri setleri oluşturulamadı. Hata:", e)
    exit()

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

# Eğitim ve test veri setleri için 'Power (W)' ve 'Temperature' tahminleri
train_data_with_predictions = X_train.copy()
train_data_with_predictions['Actual Power (W)'] = y_train
train_data_with_predictions['Predicted Power (W)'] = y_train_pred

test_data_with_predictions = X_test.copy()
test_data_with_predictions['Actual Power (W)'] = y_test
test_data_with_predictions['Predicted Power (W)'] = y_test_pred

# Tahmin edilen 'Power (W)' ve 'Temperature' değerlerini yazdırma
print("\nEğitim veri setindeki 'Power (W)' ve 'Temperature' tahminleri:")
print(train_data_with_predictions[['Actual Power (W)', 'Predicted Power (W)']].head())

print("\nTest veri setindeki 'Power (W)' ve 'Temperature' tahminleri:")
print(test_data_with_predictions[['Actual Power (W)', 'Predicted Power (W)']].head())

