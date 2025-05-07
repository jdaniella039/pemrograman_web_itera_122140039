# Sistem Manajemen Perpustakaan Sederhana

Tugas praktikum Pemrograman Web: Sistem manajemen perpustakaan dengan konsep OOP Python.

## Fitur

- Tambah item (buku/majalah)
- Tampilkan semua item yang tersedia
- Cari item berdasarkan judul atau ID

## Konsep OOP yang Digunakan

- Abstract Class (`LibraryItem`)
- Inheritance (`Book`, `Magazine`)
- Polymorphism (override `display_info`)
- Encapsulation (`_protected`, `__private`)
- Property Decorator (`@property` pada `id` dan `title`)

## Cara Menjalankan

```bash
python main.py
```

Gunakan menu CLI yang tersedia untuk mengelola perpustakaan.
