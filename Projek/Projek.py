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
            data = line.strip().split("|")
            if len(data) == 5:
                products.append(data[0], data[1], data[2], int(data[3]), int(data[4]))

def save_file():
    with open(FILE, "w") as f:
        current = products.head
        while current:
            f.write(f"{current.id}|{current.name}|{current.category}|{current.price}|{current.stock}\n")
            current = current.next

def print_header():
    print(f"\n{'ID':<8} {'Nama':<20} {'Kategori':<14} {'Harga':>10} {'Stok':>6}")
    print("-" * 62)

def print_row(node):
    print(f"{node.id:<8} {node.name:<20} {node.category:<14} {node.price:>10,} {node.stock:>6}")

def display(nodes=None):
    nodes = nodes if nodes is not None else products.to_list()
    print_header()
    if not nodes:
        print("  (tidak ada data)")
    else:
        for node in nodes:
            print_row(node)
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
    id = input("\nID produk yang ingin diubah: ").strip()
    p  = products.find_by_id(id)
    if not p:
        print("Produk tidak ditemukan."); return

    name     = input(f"Nama baru     [{p.name}]     : ").strip()
    category = input(f"Kategori baru [{p.category}] : ").strip()
    price    = input(f"Harga baru    [{p.price}]    : ").strip()
    stock    = input(f"Stok baru     [{p.stock}]    : ").strip()

    if name:     p.name     = name
    if category: p.category = category
    if price:    p.price    = int(price)
    if stock:    p.stock    = int(stock)

    save_file()
    print("Data berhasil diperbarui.")

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
    pass

def search_product():
    pass

def main_buyer():
    while True:
        print("\n========================================")
        print("             MENU PEMBELI               ")
        print("========================================")
        print("1. Lihat Semua Produk")
        print("2. Urutkan Produk")
        print("3. Cari Produk")
        print("0. Kembali")
        print("========================================")
        pilihan = input("Pilih menu: ")
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
        print("\n========================================")
        print("             MENU PENJUAL               ")
        print("========================================")
        print("1. Tambah Produk")
        print("2. Lihat Semua Produk")
        print("3. Ubah Produk")
        print("4. Hapus Produk")
        print("5. Urutkan Produk")
        print("6. Cari Produk")
        print("0. Kembali")
        print("========================================")
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
        print("\n========================================")
        print("             MENU LOGIN                 ")
        print("========================================")
        print("1. Masuk sebagai Pembeli")
        print("2. Masuk sebagai Penjual")
        print("0. Keluar")
        print("========================================")
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
