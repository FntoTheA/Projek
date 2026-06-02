# ================================================================================
# Nama Kelompok: 02J
# Anggota Kelompok: 1. Azhar Fawwaz Haris (Ketua) / A2 / J0403251043
#                   2. Azzura Mori / A1 / J0403251074
#                   3. Fuad Nizard Attaqi / A1 / J0403251086
# Judul: Sistem Kategori Produk Shopping
# ================================================================================

import os
import time

FILE = "data_produk.txt"

# LL untuk data
class Node:
    def __init__(self, id, name, category, price, stock):
        self.id       = id
        self.name     = name
        self.category = category
        self.price    = price
        self.stock    = stock
        self.next     = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, id, name, category, price, stock):
        new_node = Node(id, name, category, price, stock)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    #SequentialSearch
    def find_by_id(self, id):
        current = self.head
        while current:
            if current.id == id:
                return current
            current = current.next
        return None

    def find_by_name(self, keyword):
        results = []
        current = self.head
        while current:
            if keyword.lower() in current.name.lower():
                results.append(current)
            current = current.next
        return results

    def find_by_category(self, category):
        results = []
        current = self.head
        while current:
            if category.lower() in current.category.lower():
                results.append(current)
            current = current.next
        return results

    # Generic Merge Sort
    def mergeSort(self, head, criteria):
        if not head or not head.next:
            return head
        
        middle = self.getmiddle(head)
        next_middle = middle.next
        middle.next = None
        
        left = self.mergeSort(head, criteria)
        right = self.mergeSort(next_middle, criteria)
        
        return self.sortedMerge(left, right, criteria)

    def getmiddle(self, head):
        if not head:
            return head
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sortedMerge(self, a, b, criteria):
        if not a:
            return b
        if not b:
            return a
        
        val_a = getattr(a, criteria)
        val_b = getattr(b, criteria)
        
        if val_a <= val_b:
            result = a
            result.next = self.sortedMerge(a.next, b, criteria)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next, criteria)
        return result

    def sortingUrutanAbjad(self):
        self.head = self.mergeSort(self.head, "name")

    def sortingBerdasarkanKategori(self):
        self.head = self.mergeSort(self.head, "category")

    def sortingBerdasarkanHarga(self):
        self.head = self.mergeSort(self.head, "price")

    def sortingBerdasarkanStok(self):
        self.head = self.mergeSort(self.head, "stock")
        
    def delete(self, id):
        if not self.head:
            return False
        if self.head.id == id:
            self.head = self.head.next
            return True
        prev, current = self.head, self.head.next
        while current:
            if current.id == id:
                prev.next = current.next
                return True
            prev, current = current, current.next
        return False

    def to_list(self):
        result  = []
        current = self.head
        while current:
            result.append(current)
            current = current.next
        return result

products = LinkedList()

#Load, save, dan show File dengan template
def load_file():
    products.head = None
    if not os.path.exists(FILE):
        return
    with open(FILE) as f:
        for line in f:
            data = [x.strip() for x in line.strip().split(",")]
            if len(data) == 5:
                products.append(data[0], data[1], data[2], int(data[3]), int(data[4]))

def save_file():
    with open(FILE, "w") as f:
        current = products.head
        while current:
            f.write(f"{current.id},{current.name},{current.category},{current.price},{current.stock}\n")
            current = current.next

def print_header(max_name=30, max_cat=20):
    print(f"\n{'ID':<8} {'Nama':<{max_name}} {'Kategori':<{max_cat}} {'Harga':>10} {'Stok':>6}")
    total_len = 8 + 1 + max_name + 1 + max_cat + 1 + 10 + 1 + 6
    print("-" * total_len)

def print_row(node, max_name=30, max_cat=20):
    print(f"{node.id:<8} {node.name:<{max_name}} {node.category:<{max_cat}} {node.price:>10,} {node.stock:>6}")

def display(nodes=None):
    nodes = nodes if nodes is not None else products.to_list()
    if not nodes:
        print_header()
        print("  (tidak ada data)")
    else:
        max_name = max(30, max(len(node.name) for node in nodes))
        max_cat = max(20, max(len(node.category) for node in nodes))
        print_header(max_name, max_cat)
        for node in nodes:
            print_row(node, max_name, max_cat)

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

    category = input("Kategori   : ").strip()
    if not category:
        print("\n[ERROR] Kategori tidak boleh kosong.")
        return
    category = category.title()

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
    print("[SUCCESS] Produk berhasil ditambahkan!")
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
            category = input(f"Kategori baru [{p.category}]: ").strip()
            if category: 
                p.category = category.title()
                print("\n[SUCCESS] Kategori berhasil diubah.")
                
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
        print("\n==================================================")
        print("                  MENU PEMBELI                    ")
        print("==================================================")
        print(" [1] Lihat Semua Produk")
        print(" [2] Urutkan Produk")
        print(" [3] Cari Produk")
        print(" [4] Beli Produk")
        print(" [0] Kembali")
        print("==================================================")
        pilihan = input("Pilih menu (0-4): ").strip()
        if pilihan == "1":
            view_product()
        elif pilihan == "2":
            sort_product()
        elif pilihan == "3":
            search_product()
        elif pilihan == "4":
            beli_produk()
        elif pilihan == "0":
            os.system("cls" if os.name == "nt" else "clear")
            break
        else:
            print("\n[ERROR] Pilihan tidak valid.")
        
        if pilihan != "0":
            input("\nTekan Enter untuk lanjut...")
            os.system("cls" if os.name == "nt" else "clear")

def main_seller():
    while True:
        print("\n==================================================")
        print("                  MENU PENJUAL                    ")
        print("==================================================")
        print(" [1] Tambah Produk")
        print(" [2] Lihat Semua Produk")
        print(" [3] Ubah Produk")
        print(" [4] Hapus Produk")
        print(" [5] Urutkan Produk")
        print(" [6] Cari Produk")
        print(" [0] Kembali")
        print("==================================================")
        pilihan = input("Pilih menu (0-6): ").strip()
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
        elif pilihan == "0":
            os.system("cls" if os.name == "nt" else "clear")
            break
        else:
            print("\n[ERROR] Pilihan tidak valid.")
        
        if pilihan != "0":
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

     🛒 SISTEM KATEGORI PRODUK 🛒
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
            show_buyer_logo()
            main_buyer()
        elif pilihan == "2":
            os.system("cls" if os.name == "nt" else "clear")
            show_seller_logo()
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
