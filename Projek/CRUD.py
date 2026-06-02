from FileHandling import *
from ProjekMenu import *
from Tree import *
from LinkedList import *
#CRUD
def add_product():
    print("\n==================================================")
    print("                TAMBAH PRODUK BARU                ")
    print("==================================================")
    id = input("ID Produk  : ").strip()
    if not id:
        print("\n[ERROR] ID Produk tidak boleh kosong.")
        return
    if products.find_by_id(id):
        print("\n[ERROR] ID Produk sudah terdaftar.")
        return

    name     = input("Nama       : ").strip()
    if not name:
        print("\n[ERROR] Nama Produk tidak boleh kosong.")
        return
    name_title = name.title()

    # Pastikan tidak ada produk dengan nama yang sama sebelumnya
    current = products.head
    while current:
        if current.name.lower() == name_title.lower():
            print("\n[ERROR] Nama Produk sudah terdaftar.")
            return
        current = current.next

    name = name_title

    print("\n Pilih kategori produk melalui navigasi tree:")
    category = select_category_from_tree()
    if not category:
        print("\n[INFO] Penambahan produk dibatalkan.")
        return

    price_str = input("Harga      : ").strip()
    if not price_str.isdigit():
        print("\n[ERROR] Harga harus berupa angka bulat positif.")
        return
    price = int(price_str)

    stock_str = input("Stok       : ").strip()
    if not stock_str.isdigit():
        print("\n[ERROR] Stok harus berupa angka bulat positif.")
        return
    stock = int(stock_str)

    products.append(id, name, category, price, stock)
    save_file()
    print("\n==================================================")
    print(f"[SUCCESS] Produk berhasil ditambahkan! (Kategori: {category})")
    print("==================================================")

def view_product():
    print("\n==================================================")
    print("                DAFTAR SEMUA PRODUK               ")
    print("==================================================")
    display()

def update_product():
    print("\n==================================================")
    print("                 UBAH DATA PRODUK                 ")
    print("==================================================")
    display()
    id = input("\nPilih produk yang ingin diubah (ID): ").strip()
    p  = products.find_by_id(id)
    
    if not p:
        print("\n[ERROR] Produk tidak ditemukan.")
        return

    while True:
        print("\n==================================================")
        print(f"            UBAH DATA PRODUK: {p.id}")
        print("==================================================")
        print(f" [1] Nama     : {p.name}")
        print(f" [2] Kategori : {p.category}")
        print(f" [3] Harga    : Rp {p.price:,}")
        print(f" [4] Stok     : {p.stock}")
        print(" [0] Selesai & Simpan")
        print("==================================================")
        
        pilihan = input("Pilih menu (0-4): ").strip()
        
        if pilihan == "1":
            name = input(f"Nama baru [{p.name}]: ").strip()
            if name: 
                name_title = name.title()
                duplicate = False
                current = products.head
                while current:
                    if current != p and current.name.lower() == name_title.lower():
                        duplicate = True
                        break
                    current = current.next
                
                if duplicate:
                    print("\n[ERROR] Nama Produk sudah terdaftar.")
                else:
                    p.name = name_title
                    print("\n[SUCCESS] Nama berhasil diubah.")
                
        elif pilihan == "2":
            print(f"\n Kategori saat ini: {p.category}")
            print(" Pilih kategori baru melalui navigasi tree:")
            new_cat = select_category_from_tree()
            if new_cat:
                p.category = new_cat
                print(f"\n[SUCCESS] Kategori berhasil diubah ke '{new_cat}'.")
            else:
                print("\n[INFO] Perubahan kategori dibatalkan.")
                
        elif pilihan == "3":
            price = input(f"Harga baru [{p.price}]: ").strip()
            if price.isdigit(): 
                p.price = int(price)
                print("\n[SUCCESS] Harga berhasil diubah.")
            elif price:
                print("\n[ERROR] Harga harus berupa angka bulat positif.")
                
        elif pilihan == "4":
            stock = input(f"Stok baru [{p.stock}]: ").strip()
            if stock.isdigit(): 
                p.stock = int(stock)
                print("\n[SUCCESS] Stok berhasil diubah.")
            elif stock:
                print("\n[ERROR] Stok harus berupa angka bulat positif.")
                
        elif pilihan == "0":
            save_file()
            print("\n[SUCCESS] Data berhasil diperbarui dan disimpan!")
            break
            
        else:
            print("\n[ERROR] Pilihan tidak valid.")

def delete_product():
    print("\n==================================================")
    print("                   HAPUS PRODUK                   ")
    print("==================================================")
    display()
    id = input("\nMasukkan ID produk yang ingin dihapus: ").strip()
    p  = products.find_by_id(id)
    if not p:
        print("\n[ERROR] Produk tidak ditemukan.")
        return

    print("\n--------------------------------------------------")
    confirm = input(f"Apakah Anda yakin ingin menghapus '{p.name}'? (y/n): ")
    if confirm.lower() == "y":
        products.delete(id)
        save_file()
        print(f"\n[SUCCESS] '{p.name}' berhasil dihapus.")
    else:
        print("\n[INFO] Penghapusan dibatalkan.")

def beli_produk():
    print("\n==================================================")
    print("                 BELI PRODUK                      ")
    print("==================================================")
    display()
    print("\nPilih Metode Pencarian:")
    print(" [1] Berdasarkan ID")
    print(" [2] Berdasarkan Nama")
    print(" [0] Kembali")
    print("--------------------------------------------------")
    pilihan = input("Pilih metode (0-2): ").strip()
    p = None
    if pilihan == "0":
        return
    elif pilihan == "1":
        id = input("Masukkan ID Produk: ").strip()
        p = products.find_by_id(id)
        if not p:
            print("\n[ERROR] Produk dengan ID tersebut tidak ditemukan.")
            return
    elif pilihan == "2":
        name = input("Masukkan Nama Produk: ").strip()
        results = products.find_by_name(name)
        if not results:
            print("\n[ERROR] Produk dengan nama tersebut tidak ditemukan.")
            return
        if len(results) == 1:
            p = results[0]
        else:
            print("\n==================================================")
            print("             HASIL PENCARIAN PRODUK               ")
            print("==================================================")
            display(results)
            print("--------------------------------------------------")
            id_pilihan = input("Pilih ID produk yang ingin dibeli: ").strip()
            for item in results:
                if item.id == id_pilihan:
                    p = item
                    break
            if not p:
                print("\n[ERROR] ID produk tidak valid atau tidak ada di hasil pencarian.")
                return
    else:
        print("\n[ERROR] Pilihan tidak valid.")
        return
    
    while True:
        print("\n==================================================")
        print("              KONFIRMASI PEMBELIAN                ")
        print("==================================================")
        print(f" Nama Produk : {p.name}")
        print(f" ID Produk   : {p.id}")
        print(f" Kategori    : {p.category}")
        print(f" Harga       : Rp {p.price:,}")
        print(f" Stok Tersedia: {p.stock}")
        print("--------------------------------------------------")
        print(" [1] Lanjutkan Pembelian")
        print(" [0] Batal / Kembali")
        print("==================================================")
        
        pilihan = input("Pilih menu (0-1): ").strip()
        
        if pilihan == "1":
            jumlah_str = input("Masukkan Jumlah Pembelian: ").strip()
            if not jumlah_str.isdigit():
                print("\n[ERROR] Jumlah harus berupa angka bulat positif.")
                continue
            jumlah = int(jumlah_str)
            if jumlah <= 0:
                print("\n[ERROR] Jumlah pembelian harus lebih dari 0.")
            elif jumlah > p.stock:
                print("\n[ERROR] Stok tidak mencukupi.")
            else:
                p.stock -= jumlah
                save_file()
                total_harga = jumlah * p.price
                print("\n==================================================")
                print("               STRUK PEMBELIAN                    ")
                print("==================================================")
                print(f" Produk      : {p.name}")
                print(f" Jumlah      : {jumlah} pcs")
                print(f" Harga/pc    : Rp {p.price:,}")
                print("--------------------------------------------------")
                print(f" TOTAL BAYAR : Rp {total_harga:,}")
                print("==================================================")
                print("[SUCCESS] Pembelian berhasil diselesaikan!")
                break
        elif pilihan == "0":
            break
        else:
            print("\n[ERROR] Pilihan tidak valid.")