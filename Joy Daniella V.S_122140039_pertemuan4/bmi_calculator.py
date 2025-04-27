# Input berat dan tinggi badan
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (cm): "))

# Konversi tinggi dari cm ke meter
tinggi = tinggi / 100

# Hitung BMI
bmi = berat / (tinggi * tinggi)

# Tentukan kategori BMI
if bmi < 18.5:
    kategori = "Berat badan kurang"
elif 18.5 <= bmi < 25:
    kategori = "Berat badan normal"
elif 25 <= bmi < 30:
    kategori = "Berat badan berlebih"
else:
    kategori = "Obesitas"

# Tampilkan hasil
print(f"\nHasil perhitungan BMI Anda: {bmi:.2f}")
print(f"Kategori BMI: {kategori}")
