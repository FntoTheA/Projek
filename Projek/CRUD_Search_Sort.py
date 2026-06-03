# from Tree import *
from LinkedList import *
from FileHandling import *
from Tree import *
#CRUD
def add_product():
    """
    Menambahkan produk baru ke dalam sistem. Pengguna diminta menginput ID, Nama,
    Kategori (melalui navigasi tree), Harga, dan Stok. Produk baru kemudian ditambahkan
    ke dalam Linked List dan perubahan disimpan ke file.
    """
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
    from Tree import select_category_from_tree
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
    """
    Menampilkan tabel daftar seluruh produk yang ada di sistem ke terminal.
    """
    print("\n==================================================")
    print("                DAFTAR SEMUA PRODUK               ")
    print("==================================================")
    display()

def update_product():
    """
    Mengubah data spesifik dari suatu produk (Nama, Kategori, Harga, atau Stok) berdasarkan ID produk.
    Pengguna dapat melakukan beberapa pembaruan data secara interaktif sebelum akhirnya disimpan.
    """
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
            from Tree import select_category_from_tree
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
    """
    Menghapus produk dari sistem berdasarkan ID produk. Pengguna dimintai konfirmasi (y/n)
    sebelum produk benar-benar dihapus dari Linked List dan file penyimpanan diperbarui.
    """
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
    """
    Memandu alur pembelian produk oleh pembeli. Pembeli dapat mencari produk lewat ID atau Nama,
    menginputkan jumlah pembelian, memeriksa ketersediaan stok, memotong stok jika memadai,
    dan mencetak struk/nota pembelian sebagai bukti transaksi.
    """
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

def sort_product():
    """
    Menampilkan menu pengurutan produk. Pengguna dapat mengurutkan berdasarkan nama (abjad),
    kategori, harga, atau stok. Pengurutan dilakukan menggunakan Merge Sort pada Linked List.
    """
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
    """
    Menyediakan menu pencarian produk dengan beberapa filter: Nama, ID, atau Kategori.
    Hasil pencarian yang cocok akan langsung ditampilkan dalam format tabel di terminal.
    """
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