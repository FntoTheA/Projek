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