# Student Dashboard – Praktikum Pemrograman Web 2

## 📌 Fungsi Aplikasi
Aplikasi **Student Dashboard** adalah aplikasi berbasis web yang dirancang untuk membantu mahasiswa dalam mengelola:
- **Jadwal Kuliah**
- **Daftar Tugas**
- **Catatan Pribadi**

Semua data disimpan menggunakan **localStorage**, sehingga data tetap tersimpan meskipun halaman di-refresh.

## ✨ Fitur-Fitur Aplikasi
- **Jadwal Kuliah**: Tambah dan hapus mata kuliah. Data bersifat permanen.
- **Daftar Tugas**: Tambah dan hapus tugas yang akan dikerjakan. Data juga tersimpan permanen.
- **Catatan Pribadi**: Menyimpan dan menampilkan catatan terakhir.
- **Jam Digital (Real-time Clock)**: Menampilkan jam yang terus berjalan secara real-time.
- **Navigasi Tab Interaktif**: Navigasi antar fitur dilakukan melalui tab yang mudah digunakan.

## 💡 Fitur ES6+ yang Diimplementasikan
- `Arrow Function` → contoh: `const updateClock = () => { ... }`
- `Template Literals` → contoh: `` `Halo, ${name}` ``
- `Destructuring Assignment` → contoh: `const { hours, minutes } = now`
- `Spread Operator` → contoh: `[...items, newItem]`
- `Rest Parameter` → digunakan saat menambahkan item dinamis
- `Modules (Import/Export)` → memisahkan fungsi ke dalam `utils.js` dan mengimpornya ke `script.js`
- `Optional Chaining (?.)` → contoh: `inputField?.value`
- `Nullish Coalescing Operator (??)` → contoh: `savedNote ?? ''`

## 🖼️ Tampilan Aplikasi
![Student Dashboard](./Screenshot%202025-04-13%20191439.png)
