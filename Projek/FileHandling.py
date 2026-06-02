import os
from ProjekMenu import *
from Tree import *
from LinkedList import *

FILE = "data_produk.txt"
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