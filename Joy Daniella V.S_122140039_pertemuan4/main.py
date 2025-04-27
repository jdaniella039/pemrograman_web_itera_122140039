# main.py

# Cara import 1: import seluruh modul
import math_operations

# Cara import 2: import fungsi tertentu
from math_operations import luas_persegi_panjang, keliling_persegi_panjang

# Hitung luas dan keliling persegi
sisi = 5
print(f"Luas Persegi (sisi={sisi}): {math_operations.luas_persegi(sisi)}")
print(f"Keliling Persegi (sisi={sisi}): {math_operations.keliling_persegi(sisi)}\n")

# Hitung luas dan keliling persegi panjang
panjang = 8
lebar = 4
print(f"Luas Persegi Panjang (p={panjang}, l={lebar}): {luas_persegi_panjang(panjang, lebar)}")
print(f"Keliling Persegi Panjang (p={panjang}, l={lebar}): {keliling_persegi_panjang(panjang, lebar)}\n")

# Hitung luas dan keliling lingkaran
jari_jari = 7
print(f"Luas Lingkaran (r={jari_jari}): {math_operations.luas_lingkaran(jari_jari):.2f}")
print(f"Keliling Lingkaran (r={jari_jari}): {math_operations.keliling_lingkaran(jari_jari):.2f}\n")

# Konversi suhu
suhu_c = 25
print(f"{suhu_c}°C ke Fahrenheit: {math_operations.celsius_ke_fahrenheit(suhu_c):.2f}°F")
print(f"{suhu_c}°C ke Kelvin: {math_operations.celsius_ke_kelvin(suhu_c):.2f}K")
