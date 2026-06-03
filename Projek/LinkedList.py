# LL untuk data
class Node:
    def __init__(self, id, name, category, price, stock):
        """
        Inisialisasi node baru untuk Linked List dengan menyimpan atribut produk
        (ID, nama, kategori, harga, stok) dan penunjuk (next) ke node berikutnya.
        """
        self.id       = id
        self.name     = name
        self.category = category
        self.price    = price
        self.stock    = stock
        self.next     = None

class LinkedList:
    def __init__(self):
        """
        Inisialisasi Linked List kosong dengan pointer head bernilai None.
        """
        self.head = None

    def append(self, id, name, category, price, stock):
        """
        Menambahkan node produk baru ke akhir Linked List.
        """
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
        """
        Mencari produk berdasarkan ID menggunakan algoritma Sequential Search.
        Mengembalikan node produk jika ditemukan, atau None jika tidak ditemukan.
        """
        current = self.head
        while current:
            if current.id == id:
                return current
            current = current.next
        return None

    def find_by_name(self, keyword):
        """
        Mencari produk berdasarkan kata kunci nama produk secara case-insensitive.
        Mengembalikan list yang berisi semua node produk yang cocok.
        """
        results = []
        current = self.head
        while current:
            if keyword.lower() in current.name.lower():
                results.append(current)
            current = current.next
        return results

    def find_by_category(self, category):
        """
        Mencari produk berdasarkan nama kategori secara case-insensitive.
        Mengembalikan list yang berisi semua node produk yang termasuk dalam kategori tersebut.
        """
        results = []
        current = self.head
        while current:
            if category.lower() in current.category.lower():
                results.append(current)
            current = current.next
        return results

    # Generic Merge Sort
    def mergeSort(self, head, criteria):
        """
        Mengurutkan Linked List secara rekursif menggunakan algoritma Merge Sort
        berdasarkan kriteria (atribut produk) tertentu.
        """
        if not head or not head.next:
            return head
        
        middle = self.getmiddle(head)
        next_middle = middle.next
        middle.next = None
        
        left = self.mergeSort(head, criteria)
        right = self.mergeSort(next_middle, criteria)
        
        return self.sortedMerge(left, right, criteria)

    def getmiddle(self, head):
        """
        Mencari node tengah dari Linked List menggunakan teknik slow dan fast pointer.
        Digunakan sebagai pembagi list pada proses Merge Sort.
        """
        if not head:
            return head
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sortedMerge(self, a, b, criteria):
        """
        Menggabungkan dua sub-list Linked List yang sudah terurut menjadi satu Linked List
        yang terurut utuh berdasarkan kriteria yang ditentukan.
        """
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
        """
        Mengurutkan Linked List produk berdasarkan nama secara alfabetis (A-Z).
        """
        self.head = self.mergeSort(self.head, "name")

    def sortingBerdasarkanKategori(self):
        """
        Mengurutkan Linked List produk berdasarkan nama kategori secara alfabetis (A-Z).
        """
        self.head = self.mergeSort(self.head, "category")

    def sortingBerdasarkanHarga(self):
        """
        Mengurutkan Linked List produk berdasarkan harga secara menaik (murah ke mahal).
        """
        self.head = self.mergeSort(self.head, "price")

    def sortingBerdasarkanStok(self):
        """
        Mengurutkan Linked List produk berdasarkan jumlah stok secara menaik (sedikit ke banyak).
        """
        self.head = self.mergeSort(self.head, "stock")
        
    def delete(self, id):
        """
        Menghapus node produk dari Linked List berdasarkan ID produk.
        Mengembalikan True jika penghapusan berhasil, dan False jika ID produk tidak ditemukan.
        """
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
        """
        Mengonversi struktur data Linked List menjadi list biasa (array-like) di Python.
        Mengembalikan list yang berisi objek-objek Node produk.
        """
        result  = []
        current = self.head
        while current:
            result.append(current)
            current = current.next
        return result

