import os

class Node:
    def __init__(self, id_produk, nama, kategori, harga, stok):
        self.id_produk = id_produk
        self.nama = nama
        self.kategori = kategori
        self.harga = harga
        self.stok = stok
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, id_produk, nama, kategori, harga, stok):
        node_baru = Node(id_produk, nama, kategori, harga, stok)

        if self.head is None:
            self.head = node_baru
        else:
            sekarang = self.head
            while sekarang.next is not None:
                sekarang = sekarang.next
            sekarang.next = node_baru

    def cari(self, id_produk):
        sekarang = self.head
        while sekarang is not None:
            if sekarang.id_produk == id_produk:
                return sekarang
            sekarang = sekarang.next
        return None

    def hapus(self, id_produk):
        if self.head is None:
            return False

        if self.head.id_produk == id_produk:
            self.head = self.head.next
            return True

        sebelum = self.head
        sekarang = self.head.next
        while sekarang is not None:
            if sekarang.id_produk == id_produk:
                sebelum.next = sekarang.next
                return True
            sebelum = sekarang
            sekarang = sekarang.next

        return False 

NAMA_FILE = "data_produk.txt"
daftar_produk = LinkedList()

def baca_file():
    daftar_produk.head = None

    if not os.path.exists(NAMA_FILE):
        return

    file = open(NAMA_FILE, "r")
    for baris in file:
        baris = baris.strip()
        if baris == "":
            continue
        data = baris.split("|")
        if len(data) == 5:
            daftar_produk.tambah(data[0], data[1], data[2], int(data[3]), int(data[4]))
    file.close()

def simpan_file():
    file = open(NAMA_FILE, "w")
    sekarang = daftar_produk.head
    while sekarang is not None:
        file.write(f"{sekarang.id_produk}|{sekarang.nama}|{sekarang.kategori}|{sekarang.harga}|{sekarang.stok}\n")
        sekarang = sekarang.next
    file.close()

def tambah_produk():
    print("\n--- TAMBAH PRODUK BARU ---")
    id_produk = input("ID Produk (contoh P006) : ")

    if daftar_produk.cari(id_produk) is not None:
        print("ID sudah ada! Gunakan ID lain.")
        return

    nama = input("Nama Produk              : ")
    kategori = input("Kategori (Elektronik/Fashion/Makanan) : ")
    harga = int(input("Harga                    : "))
    stok = int(input("Stok                     : "))

    daftar_produk.tambah(id_produk, nama, kategori, harga, stok)
    simpan_file()
    print(f"Produk '{nama}' berhasil ditambahkan!")

def lihat_produk():
    print("\n--- DAFTAR SEMUA PRODUK ---")
    print("=" * 70)
    print(f"{'ID':<8} {'Nama':<20} {'Kategori':<12} {'Harga':>10} {'Stok':>6}")
    print("=" * 70)

    sekarang = daftar_produk.head

    if sekarang is None:
        print("Belum ada data produk.")
    else:
        while sekarang is not None:
            print(f"{sekarang.id_produk:<8} {sekarang.nama:<20} {sekarang.kategori:<12} {sekarang.harga:>10,} {sekarang.stok:>6}")
            sekarang = sekarang.next

    print("=" * 70)

def ubah_produk():
    print("\n--- UBAH DATA PRODUK ---")
    lihat_produk()

    id_produk = input("\nMasukkan ID produk yang ingin diubah: ")
    produk = daftar_produk.cari(id_produk)

    if produk is None:
        print("Produk tidak ditemukan!")
        return

    print(f"\nData saat ini: {produk.nama} | {produk.kategori} | Rp{produk.harga:,} | Stok: {produk.stok}")
    print("(Kosongkan jika tidak ingin mengubah)\n")

    nama_baru = input(f"Nama baru [{produk.nama}]       : ")
    kategori_baru = input(f"Kategori baru [{produk.kategori}] : ")
    harga_baru = input(f"Harga baru [{produk.harga}]      : ")
    stok_baru = input(f"Stok baru [{produk.stok}]        : ")

    if nama_baru != "":
        produk.nama = nama_baru
    if kategori_baru != "":
        produk.kategori = kategori_baru
    if harga_baru != "":
        produk.harga = int(harga_baru)
    if stok_baru != "":
        produk.stok = int(stok_baru)

    simpan_file()
    print("Data produk berhasil diubah!")

def hapus_produk():
    print("\n--- HAPUS PRODUK ---")
    lihat_produk()

    id_produk = input("\nMasukkan ID produk yang ingin dihapus: ")
    produk = daftar_produk.cari(id_produk)

    if produk is None:
        print("Produk tidak ditemukan!")
        return

    konfirmasi = input(f"Yakin hapus '{produk.nama}'? (y/n): ")
    if konfirmasi.lower() == "y":
        daftar_produk.hapus(id_produk)
        simpan_file()
        print(f"Produk '{produk.nama}' berhasil dihapus!")
    else:
        print("Batal menghapus.")

def menu_utama():
    baca_file()

    while True:
        print("\n========================================")
        print("   SISTEM KATEGORI PRODUK TOKO ONLINE   ")
        print("========================================")
        print("1. Tambah Produk")
        print("2. Lihat Semua Produk")
        print("3. Ubah Produk")
        print("4. Hapus Produk")
        print("0. Keluar")
        print("========================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_produk()
        elif pilihan == "2":
            lihat_produk()
        elif pilihan == "3":
            ubah_produk()
        elif pilihan == "4":
            hapus_produk()
        elif pilihan == "0":
            print("\nTerima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

        input("\nTekan Enter untuk lanjut...")
        os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    menu_utama()
