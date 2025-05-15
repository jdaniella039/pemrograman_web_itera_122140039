from abc import ABC, abstractmethod

# Abstract Class
class LibraryItem(ABC):
    def __init__(self, id, title):
        self._id = id               # protected attribute
        self._title = title

    @abstractmethod
    def display_info(self):
        pass

    @property
    def title(self):
        return self._title

    @property
    def id(self):
        return self._id

# Subclass Book
class Book(LibraryItem):
    def __init__(self, id, title, author):
        super().__init__(id, title)
        self.__author = author      # private attribute

    def display_info(self):
        print(f"[Book] ID: {self.id}, Title: {self.title}, Author: {self.__author}")

# Subclass Magazine
class Magazine(LibraryItem):
    def __init__(self, id, title, issue):
        super().__init__(id, title)
        self.__issue = issue        # private attribute

    def display_info(self):
        print(f"[Magazine] ID: {self.id}, Title: {self.title}, Issue: {self.__issue}")

# Class Library
class Library:
    def __init__(self):
        self.__collection = []      # private list

    def add_item(self, item):
        self.__collection.append(item)

    def show_all_items(self):
        if not self.__collection:
            print("Tidak ada item di perpustakaan.")
        else:
            for item in self.__collection:
                item.display_info()

    def search_by_title(self, title):
        found = False
        for item in self.__collection:
            if item.title.lower() == title.lower():
                item.display_info()
                found = True
        if not found:
            print("Item dengan judul tersebut tidak ditemukan.")

    def search_by_id(self, id):
        found = False
        for item in self.__collection:
            if item.id == id:
                item.display_info()
                found = True
        if not found:
            print("Item dengan ID tersebut tidak ditemukan.")

# CLI Interaktif
def menu():
    lib = Library()
    while True:
        print("\n=== Menu Perpustakaan ===")
        print("1. Tambah Buku")
        print("2. Tambah Majalah")
        print("3. Lihat Semua Item")
        print("4. Cari berdasarkan Judul")
        print("5. Cari berdasarkan ID")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            id = int(input("ID: "))
            title = input("Judul: ")
            author = input("Penulis: ")
            lib.add_item(Book(id, title, author))
            print("Buku berhasil ditambahkan.")
        elif pilihan == "2":
            id = int(input("ID: "))
            title = input("Judul: ")
            issue = input("Edisi: ")
            lib.add_item(Magazine(id, title, issue))
            print("Majalah berhasil ditambahkan.")
        elif pilihan == "3":
            lib.show_all_items()
        elif pilihan == "4":
            title = input("Masukkan judul: ")
            lib.search_by_title(title)
        elif pilihan == "5":
            id = int(input("Masukkan ID: "))
            lib.search_by_id(id)
        elif pilihan == "0":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu()
