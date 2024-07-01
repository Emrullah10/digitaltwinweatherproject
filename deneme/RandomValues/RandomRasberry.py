import csv
import random
import time
import os
from datetime import datetime

# Başlıkları tanımla
HEADERS = ['VIL (V)', 'VIH (V)', 'IIL (µA)', 'CIN (pF)', 'VOL (V)', 'VOH (V)', 'IOL (mA)', 'IOH (mA)',
           'RPU (kΩ)', 'RPD (kΩ)', 'Power (W)']

# Maksimum değerler
MAX_VOLTAGE = 3.3  # En yüksek voltaj (V)
MAX_CURRENT = 7.0  # En yüksek akım (mA)
MAX_POWER = MAX_VOLTAGE * (MAX_CURRENT / 1000)  # En yüksek güç (W)

# Dosya yolu tanımlama
output_directory = r"C:\Users\ibrah\OneDrive\Desktop\rasberrypi_csv"  # Dosyaların kaydedilmesini istediğiniz yolu yazın
if not os.path.exists(output_directory):
    os.makedirs(output_directory)  # Belirtilen dizin yoksa oluştur

filename = os.path.join(output_directory, 'raspberry_pi_datasheet_random_data.csv')
grouped_filename = os.path.join(output_directory, 'grouped_raspberry_pi_datasheet_random_data.csv')


def generate_random_data():
    VIL = round(random.uniform(0.0, 0.8), 2)  # Input low voltage (V)
    VIH = round(random.uniform(2.0, 3.3), 2)  # Input high voltage (V)
    IIL = round(random.uniform(0.0, 10.0), 2)  # Input leakage current (µA)
    CIN = round(random.uniform(0.0, 5.0), 2)  # Input capacitance (pF)
    VOL = round(random.uniform(0.0, 0.4), 2)  # Output low voltage (V)
    VOH = round(random.uniform(2.9, 3.3), 2)  # Output high voltage (V)
    IOL = round(random.uniform(7.0, 7.0), 2)  # Output low current (mA)
    IOH = round(random.uniform(7.0, 7.0), 2)  # Output high current (mA)
    RPU = round(random.uniform(18.0, 73.0), 2)  # Pullup resistor (kΩ)
    RPD = round(random.uniform(18.0, 73.0), 2)  # Pulldown resistor (kΩ)
    power = VIH * (IOL / 1000)  # Güç (W)

    return {
        'VIL (V)': VIL,
        'VIH (V)': VIH,
        'IIL (µA)': IIL,
        'CIN (pF)': CIN,
        'VOL (V)': VOL,
        'VOH (V)': VOH,
        'IOL (mA)': IOL,
        'IOH (mA)': IOH,
        'RPU (kΩ)': RPU,
        'RPD (kΩ)': RPD,
        'Power (W)': round(power, 4)
    }


def write_to_csv(filename, data):
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        writer.writerow(data)


def convert_to_grouped_csv(data_list, output_filename):
    grouped_data = {header: [] for header in HEADERS}

    for data in data_list:
        for header in HEADERS:
            grouped_data[header].append(data[header])

    with open(output_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(HEADERS)
        max_length = max(len(values) for values in grouped_data.values())
        for i in range(max_length):
            row = [grouped_data[header][i] if i < len(grouped_data[header]) else '' for header in HEADERS]
            writer.writerow(row)


def main():
    data_list = []

    # CSV dosyasına başlık ekleme
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        writer.writeheader()

    try:
        while True:
            data = generate_random_data()
            data_list.append(data)
            write_to_csv(filename, data)
            print(f"Data written: {data}")
            time.sleep(5)  # 5 saniye bekle
    except KeyboardInterrupt:
        print("Data generation stopped.")

    # Verileri başlıklarına göre gruplandırılmış şekilde yeni CSV dosyasına yaz
    convert_to_grouped_csv(data_list, grouped_filename)


if __name__ == "__main__":
    main()
