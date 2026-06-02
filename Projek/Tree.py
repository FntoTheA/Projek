# Tree untuk kategori bertingkat
from ProjekMenu import *
from LinkedList import *
from FileHandling import *


class CategoryTreeNode:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []  # List of CategoryTreeNode

    def add_child(self, name):
        child = CategoryTreeNode(name, parent=self)
        self.children.append(child)
        return child

    def find_child(self, name):
        for child in self.children:
            if child.name.lower() == name.lower():
                return child
        return None

    def get_all_leaf_names(self):
        """Mengambil semua nama kategori di node ini dan sub-node secara rekursif"""
        if not self.children:
            return [self.name]
        result = [self.name]
        for child in self.children:
            result.extend(child.get_all_leaf_names())
        return result

def build_category_tree():
    """Membangun tree kategori yang sudah ditetapkan"""
    root = CategoryTreeNode("Kategori Utama")

    makanan = root.add_child("Makanan")
    makanan.add_child("Snack")
    makanan.add_child("Minuman")

    root.add_child("Buah")
    root.add_child("Hewan")

    elektronik = root.add_child("Elektronik")
    elektronik.add_child("HP")
    elektronik.add_child("Laptop")

    fashion = root.add_child("Fashion")
    fashion.add_child("Aksesoris")

    root.add_child("Mainan")
    root.add_child("Tiket")
    root.add_child("Jasa")
    root.add_child("Obat")

    return root
# Fungsi navigasi tree untuk menjelajahi kategori (Pembeli & Penjual)
def browse_categories():
    """Menu interaktif untuk menjelajahi kategori bertingkat"""
    root = build_category_tree()
    current = root

    while True:
        os.system("cls" if os.name == "nt" else "clear")

        # Tampilkan path navigasi
        path = []
        node = current
        while node:
            path.append(node.name)
            node = node.parent
        path_str = " > ".join(reversed(path))

        print(f"\n{'='*50}")
        print(f"  {path_str}")
        print(f"{'='*50}")

        # Tampilkan subkategori
        if current.children:
            print(" Subkategori:")
            for idx, child in enumerate(current.children, 1):
                print(f"  [{idx}] {child.name}")
            print("-" * 50)

        # Ambil produk yang cocok dengan kategori ini & semua sub-nya
        valid_names = current.get_all_leaf_names()
        matching = []
        p = products.head
        while p:
            if p.category in valid_names:
                matching.append(p)
            p = p.next

        if matching:
            print(f"\n Produk ({len(matching)} item):")
            display(matching)
        else:
            print("\n  (tidak ada produk di kategori ini)")

        print(f"\n{'='*50}")
        if current.parent:
            print(" [0] Kembali ke atas")
        else:
            print(" [0] Keluar dari penjelajahan")
        if current.children:
            print(f" [1-{len(current.children)}] Pilih subkategori")
        print(f"{'='*50}")

        pilihan = input("Pilih: ").strip()
        if pilihan == "0":
            if current.parent:
                current = current.parent
            else:
                break
        elif current.children and pilihan.isdigit() and 1 <= int(pilihan) <= len(current.children):
            current = current.children[int(pilihan) - 1]
        else:
            print("\n[ERROR] Pilihan tidak valid.")
            input("Tekan Enter untuk lanjut...")

# Fungsi pemilihan kategori via tree (untuk add/update produk)
def select_category_from_tree():
    """Navigasi tree untuk memilih kategori produk. Return nama kategori atau None jika batal."""
    root = build_category_tree()
    current = root

    while True:
        # Tampilkan path navigasi
        path = []
        node = current
        while node:
            path.append(node.name)
            node = node.parent
        path_str = " > ".join(reversed(path))

        print(f"\n{'='*50}")
        print(f"  PILIH KATEGORI: {path_str}")
        print(f"{'='*50}")

        if current.children:
            for idx, child in enumerate(current.children, 1):
                print(f"  [{idx}] {child.name}")

        print("-" * 50)
        if current != root:
            print(f"  [P] Pilih '{current.name}' sebagai kategori")
            print(f"  [0] Kembali")
        else:
            print(f"  [0] Batal")
        print("-" * 50)

        pilihan = input("Pilih: ").strip().upper()

        if pilihan == "0":
            if current == root:
                return None
            current = current.parent
        elif pilihan == "P" and current != root:
            return current.name
        elif current.children and pilihan.isdigit() and 1 <= int(pilihan) <= len(current.children):
            current = current.children[int(pilihan) - 1]
        else:
            print("[ERROR] Pilihan tidak valid.")