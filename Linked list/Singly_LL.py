class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class SinglyLL:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, data):
        
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        
        self.tail.next = newNode
        self.tail = newNode
        
    def display(self):
        temp = self.head
        
        while temp:
            print(temp.data, end = '->')
            temp = temp.next
        
        print('None')
        
    def insert_at_start(self, data):
        
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return 
        
        newNode.next = self.head
        self.head = newNode
        
    
    def insert_at_last(self, data):
        newNode = Node(data)
        if self.tail is None:
            self.tail = newNode
            self.head = newNode
            return
        
        self.tail.next = newNode
        self.tail = newNode
        
    def insert_at_Kth(self, data, k):
        
        newNode = Node(data)
        
        cur = self.head
        for i in range(k-1):
            cur = cur.next
            
        newNode.next = cur.next
        cur.next = newNode
        
l = SinglyLL()
l.append(1)
l.append(2)
l.append(3)
l.append(4)

l.display()
l.insert_at_start(0)
l.display()
l.insert_at_last(5)
l.display()
l.insert_at_Kth(3.5, 4)
l.display()
