import csv
import random

# Verilen veriler
voc = (4.6, 0.08)  # Voltaj (Voc)
isc = (0.11, 0.08)  # Akım (Isc)


# Elektrik gücünü hesaplayan fonksiyon
def calculate_power(voltage, current):
    return round(voltage * current, 2)


# Rastgele veri üretme fonksiyonu
def generate_random_data():
    # Voltaj değeri
    random_voltage = random.uniform(voc[0] - (voc[0] * voc[1]), voc[0] + (voc[0] * voc[1]))

    # Akım değeri
    random_current = random.uniform(isc[0] - (isc[0] * isc[1]), isc[0] + (isc[0] * isc[1]))

    # Elektrik gücü (watt) değeri
    random_power = calculate_power(random_voltage, random_current)

    return {
        "Open Circuit Voltage(Voc)": round(random_voltage, 2),
        "Short Circuit Current (Isc)": round(random_current, 2),
        "Power (W)": random_power
    }


# CSV dosyasına verileri yazma fonksiyonu
def write_to_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)


# Rastgele veri üret
random_data = generate_random_data()

# Dosya yolu
file_path = r"C:\Users\ibrah\OneDrive\Desktop\solarpanel_csv\random_data.csv"

# CSV dosyasına verileri yaz
write_to_csv(file_path, random_data)

print(f"Veriler '{file_path}' dosyasına başarıyla kaydedildi.")
