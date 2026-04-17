# ================================================================================
# Nama Kelompok: 02J
# Anggota Kelompok: 1. Azhar Fawwaz Haris (Ketua) / A2
#                   2. Azzura Mori / A1
#                   3. Fuad Nizard Attaqi / A1
# Judul: Sistem Kategori Produk Shopping
# Progress : 40%
# ================================================================================

import os

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
            data = line.strip().split(",")
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
#CRUD
def add_product():
    id = input("ID Produk  : ").strip()
    if products.find_by_id(id):
        print("ID sudah ada."); return

    name     = input("Nama       : ").strip()
    category = input("Kategori   : ").strip()
    price    = int(input("Harga      : "))
    stock    = int(input("Stok       : "))

    products.append(id, name, category, price, stock)
    save_file()
    print(f"'{name}' berhasil ditambahkan.")

def view_product():
    display()

def update_product():
    display()
    id = input("\nPilih produk (ID): ").strip()
    p  = products.find_by_id(id)
    
    if not p:
        print("Produk tidak ditemukan.")
        return

    while True:
        print("\n===")
        print(f"UBAH DATA PRODUK: {p.id}")
        print("===")
        print(f"1. Nama     : {p.name}")
        print(f"2. Kategori : {p.category}")
        print(f"3. Harga    : {p.price}")
        print(f"4. Stok     : {p.stock}")
        print("0. Selesai")
        
        pilihan = input("Pilih: ").strip()
        
        if pilihan == "1":
            name = input(f"Nama baru [{p.name}]: ").strip()
            if name: 
                p.name = name
                print("Nama berhasil diubah.")
                
        elif pilihan == "2":
            category = input(f"Kategori baru [{p.category}]: ").strip()
            if category: 
                p.category = category.title()
                print("Kategori berhasil diubah.")
                
        elif pilihan == "3":
            price = input(f"Harga baru [{p.price}]: ").strip()
            if price.isdigit(): 
                p.price = int(price)
                print("Harga berhasil diubah.")
            elif price:
                print("Harga harus berupa angka.")
                
        elif pilihan == "4":
            stock = input(f"Stok baru [{p.stock}]: ").strip()
            if stock.isdigit(): 
                p.stock = int(stock)
                print("Stok berhasil diubah.")
            elif stock:
                print("Stok harus berupa angka.")
                
        elif pilihan == "0":
            save_file()
            print("\nData berhasil diperbarui dan disimpan ke file.")
            break
            
        else:
            print("Pilihan tidak valid.")

def delete_product():
    display()
    id = input("\nID produk yang ingin dihapus: ").strip()
    p  = products.find_by_id(id)
    if not p:
        print("Produk tidak ditemukan."); return

    confirm = input(f"Hapus '{p.name}'? (y/n): ")
    if confirm.lower() == "y":
        products.delete(id)
        save_file()
        print(f"'{p.name}' berhasil dihapus.")
    else:
        print("Batal.")

def sort_product():
    print("Coming soon!")
    pass

def search_product():
    print("Coming soon!")
    pass

def main_buyer():
    while True:
        print("\n===")
        print("MENU PEMBELI")
        print("===")
        print("1. Lihat Semua Produk")
        print("2. Urutkan Produk")
        print("3. Cari Produk")
        print("0. Kembali")
        pilihan = input("Pilih: ")
        if pilihan == "1":
            view_product()
        elif pilihan == "2":
            sort_product()
        elif pilihan == "3":
            search_product()
        elif pilihan == "0":
            os.system("cls" if os.name == "nt" else "clear")
            break
        else:
            print("Pilihan tidak valid")
        
        if pilihan != "0":
            input("\nTekan Enter untuk lanjut...")
            os.system("cls" if os.name == "nt" else "clear")

def main_seller():
    while True:
        print("\n===")
        print("MENU PENJUAL")
        print("===")
        print("1. Tambah Produk")
        print("2. Lihat Semua Produk")
        print("3. Ubah Produk")
        print("4. Hapus Produk")
        print("5. Urutkan Produk")
        print("6. Cari Produk")
        print("0. Kembali")

        pilihan = input("Pilih: ")
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
            print("Pilihan tidak valid")
        
        if pilihan != "0":
            input("\nTekan Enter untuk lanjut...")
            os.system("cls" if os.name == "nt" else "clear")

#Main Func
def main():
    load_file()
    while True:
        print("\n===")
        print("MENU LOGIN")
        print("===")
        print("1. Masuk sebagai Pembeli")
        print("2. Masuk sebagai Penjual")
        print("0. Keluar")
        pilihan = input("Pilih: ")
        if pilihan == "1":
            os.system("cls" if os.name == "nt" else "clear")
            main_buyer()
        elif pilihan == "2":
            os.system("cls" if os.name == "nt" else "clear")
            main_seller()
        elif pilihan == "0":
            print("\nProgram selesai.")
            break
        else:
            print("Pilihan tidak valid")
            input("\nTekan Enter untuk lanjut...")
            os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    main()
