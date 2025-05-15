# Program Pengelolaan Data Nilai Mahasiswa

# Data mahasiswa: list of dictionary
mahasiswa = [
    {"nama": "Danyl", "nim": "122140039", "nilai_uts": 80, "nilai_uas": 85, "nilai_tugas": 90},
    {"nama": "Tia", "nim": "122140040", "nilai_uts": 70, "nilai_uas": 65, "nilai_tugas": 75},
    {"nama": "Zoe", "nim": "122140041", "nilai_uts": 60, "nilai_uas": 55, "nilai_tugas": 65},
    {"nama": "Kio", "nim": "122140042", "nilai_uts": 90, "nilai_uas": 95, "nilai_tugas": 85},
    {"nama": "George", "nim": "122140043", "nilai_uts": 50, "nilai_uas": 45, "nilai_tugas": 55},
]

# Hitung nilai akhir dan tentukan grade
for mhs in mahasiswa:
    nilai_akhir = (0.3 * mhs["nilai_uts"]) + (0.4 * mhs["nilai_uas"]) + (0.3 * mhs["nilai_tugas"])
    mhs["nilai_akhir"] = round(nilai_akhir, 2)

    if nilai_akhir >= 80:
        mhs["grade"] = "A"
    elif nilai_akhir >= 70:
        mhs["grade"] = "B"
    elif nilai_akhir >= 60:
        mhs["grade"] = "C"
    elif nilai_akhir >= 50:
        mhs["grade"] = "D"
    else:
        mhs["grade"] = "E"

# Tampilkan semua data dalam format tabel
print("\nData Mahasiswa:")
print("-" * 80)
print(f"{'Nama':<15}{'NIM':<12}{'UTS':<6}{'UAS':<6}{'Tugas':<8}{'Akhir':<8}{'Grade':<6}")
print("-" * 80)
for mhs in mahasiswa:
    print(f"{mhs['nama']:<15}{mhs['nim']:<12}{mhs['nilai_uts']:<6}{mhs['nilai_uas']:<6}{mhs['nilai_tugas']:<8}{mhs['nilai_akhir']:<8}{mhs['grade']:<6}")
print("-" * 80)

# Cari mahasiswa dengan nilai tertinggi dan terendah
tertinggi = max(mahasiswa, key=lambda x: x["nilai_akhir"])
terendah = min(mahasiswa, key=lambda x: x["nilai_akhir"])

print("\nMahasiswa dengan nilai tertinggi:")
print(f"Nama: {tertinggi['nama']}, NIM: {tertinggi['nim']}, Nilai Akhir: {tertinggi['nilai_akhir']}, Grade: {tertinggi['grade']}")

print("\nMahasiswa dengan nilai terendah:")
print(f"Nama: {terendah['nama']}, NIM: {terendah['nim']}, Nilai Akhir: {terendah['nilai_akhir']}, Grade: {terendah['grade']}")
