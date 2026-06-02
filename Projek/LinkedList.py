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

