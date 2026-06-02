# ================================================================================
# Nama Kelompok: 02J
# Anggota Kelompok: 1. Azhar Fawwaz Haris (Ketua) / A2 / J0403251043
#                   2. Azzura Mori / A1 / J0403251074
#                   3. Fuad Nizard Attaqi / A1 / J0403251086
# Judul: Sistem Kategori Produk Shopping
# ================================================================================

import os
import time
from LinkedList import *
from Tree import *
from FileHandling import *
from CRUD import *

def sort_product():
    print("\n==================================================")
    print("                 URUTKAN PRODUK                   ")
    print("==================================================")
    print(" [1] Berdasarkan Nama (Abjad)") 
    print(" [2] Berdasarkan Kategori")
    print(" [3] Berdasarkan Harga")
    print(" [4] Berdasarkan Stok") 
    print(" [0] Kembali")
    print("==================================================")
    pilihan_sorting = input("Pilih menu (0-4): ").strip()
    match pilihan_sorting:
        case "1":
            products.sortingUrutanAbjad()
            print("\n[SUCCESS] Diurutkan berdasarkan Nama.")
            display()
        case "2":
            products.sortingBerdasarkanKategori()
            print("\n[SUCCESS] Diurutkan berdasarkan Kategori.")
            display()
        case "3":
            products.sortingBerdasarkanHarga()
            print("\n[SUCCESS] Diurutkan berdasarkan Harga.")
            display()
        case "4":
            products.sortingBerdasarkanStok()
            print("\n[SUCCESS] Diurutkan berdasarkan Stok.")
            display()
        case "0":
            pass
        case _:
            print("\n[ERROR] Pilihan tidak valid.")

def search_product():
    print("\n==================================================")
    print("                  CARI PRODUK                     ")
    print("==================================================")
    print(" [1] Berdasarkan Nama")
    print(" [2] Berdasarkan ID")
    print(" [3] Berdasarkan Kategori")
    print(" [0] Kembali")
    print("==================================================")
    pilihan_search = input("Pilih menu (0-3): ").strip()
    match pilihan_search:
        case "1":
            keyword = input("Masukkan Nama Produk: ").strip()
            results = products.find_by_name(keyword)
            if results: 
                print("\n==================================================")
                print("             HASIL PENCARIAN PRODUK               ")
                print("==================================================")
                display(results)
            else:
                print("\n[ERROR] Produk tidak ditemukan.")
        case "2":
            keyword = input("Masukkan ID Produk: ").strip()
            results = products.find_by_id(keyword)
            if results: 
                print("\n==================================================")
                print("             HASIL PENCARIAN PRODUK               ")
                print("==================================================")
                display([results])
            else:
                print("\n[ERROR] Produk tidak ditemukan.")
        case "3":
            category = input("Masukkan Kategori: ").strip()
            results = products.find_by_category(category)
            if results:
                print("\n==================================================")
                print("             HASIL PENCARIAN PRODUK               ")
                print("==================================================")
                display(results)
            else:
                print("\n[ERROR] Produk tidak ditemukan.")
        case "0":
            pass
        case _:
            print("\n[ERROR] Pilihan tidak valid.")


def main_buyer():
    while True:
        show_buyer_logo()
        print("\n==================================================")
        print("                  MENU PEMBELI                    ")
        print("==================================================")
        print(" [1] Lihat Semua Produk")
        print(" [2] Urutkan Produk")
        print(" [3] Cari Produk")
        print(" [4] Beli Produk")
        print(" [5] Jelajahi Kategori")
        print(" [0] Kembali")
        print("==================================================")
        pilihan = input("Pilih menu (0-5): ").strip()
        if pilihan == "1":
            view_product()
        elif pilihan == "2":
            sort_product()
        elif pilihan == "3":
            search_product()
        elif pilihan == "4":
            beli_produk()
        elif pilihan == "5":
            browse_categories()
        elif pilihan == "0":
            os.system("cls" if os.name == "nt" else "clear")
            break
        else:
            print("\n[ERROR] Pilihan tidak valid.")
        
        if pilihan != "0" and pilihan != "5":
            input("\nTekan Enter untuk lanjut...")
            os.system("cls" if os.name == "nt" else "clear")

def main_seller():
    while True:
        show_seller_logo()
        print("\n==================================================")
        print("                  MENU PENJUAL                    ")
        print("==================================================")
        print(" [1] Tambah Produk")
        print(" [2] Lihat Semua Produk")
        print(" [3] Ubah Produk")
        print(" [4] Hapus Produk")
        print(" [5] Urutkan Produk")
        print(" [6] Cari Produk")
        print(" [7] Jelajahi Kategori")
        print(" [0] Kembali")
        print("==================================================")
        pilihan = input("Pilih menu (0-7): ").strip()
        if pilihan == "1":
            add_product()
        elif pilihan == "2":
            view_product()
        elif pilihan == "3":
            update_product()
        elif pilihan == "4":
            delete_product()
        elif pilihan == "5":
            sort_product()
        elif pilihan == "6":
            search_product()
        elif pilihan == "7":
            browse_categories()
        elif pilihan == "0":
            os.system("cls" if os.name == "nt" else "clear")
            break
        else:
            print("\n[ERROR] Pilihan tidak valid.")
        
        if pilihan != "0" and pilihan != "7":
            input("\nTekan Enter untuk lanjut...")
            os.system("cls" if os.name == "nt" else "clear")

def show_logo():
    print(r"""
 ███████╗██╗  ██╗ ██████╗ ██████╗
 ██╔════╝██║  ██║██╔═══██╗██╔══██╗
 ███████╗███████║██║   ██║██████╔╝
 ╚════██║██╔══██║██║   ██║██╔═══╝
 ███████║██║  ██║╚██████╔╝██║
 ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝

   SISTEM KATEGORI PRODUK ONLINE
    """)

def show_buyer_logo():
    print(r"""
██████╗ ██╗   ██╗██╗   ██╗███████╗██████╗
██╔══██╗██║   ██║╚██╗ ██╔╝██╔════╝██╔══██╗
██████╔╝██║   ██║ ╚████╔╝ █████╗  ██████╔╝
██╔══██╗██║   ██║  ╚██╔╝  ██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝   ██║   ███████╗██║  ██║
╚═════╝  ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝
""")

def show_seller_logo():
    print(r"""
███████╗███████╗██╗     ██╗     ███████╗██████╗
██╔════╝██╔════╝██║     ██║     ██╔════╝██╔══██╗
███████╗█████╗  ██║     ██║     █████╗  ██████╔╝
╚════██║██╔══╝  ██║     ██║     ██╔══╝  ██╔══██╗
███████║███████╗███████╗███████╗███████╗██║  ██║
╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
""")

def loading_system():
    print("\nMemulai Sistem Shopping...\n")

    for i in range(0, 101, 10):
        bar = "■" * (i // 10) + "□" * (10 - i // 10)
        print(f"\r[{bar}] {i}%", end="")
        time.sleep(0.15)

    print("\n")

#Start Func
def main():

    loading_system()
    
    load_file()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        show_logo()
        print("\n==================================================")
        print("                   MENU LOGIN                     ")
        print("==================================================")
        print(" [1] Masuk sebagai Pembeli")
        print(" [2] Masuk sebagai Penjual")
        print(" [0] Keluar")
        print("==================================================")
        pilihan = input("Pilih menu (0-2): ").strip()
        if pilihan == "1":
            os.system("cls" if os.name == "nt" else "clear")
            main_buyer()
        elif pilihan == "2":
            os.system("cls" if os.name == "nt" else "clear")
            main_seller()
        elif pilihan == "0":
            print("\n[INFO] Program selesai. Sampai jumpa!")
            break
        else:
            print("\n[ERROR] Pilihan tidak valid.")
            input("\nTekan Enter untuk lanjut...")
            os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    main()
