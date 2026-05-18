class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
       
       
class SinglyLL:

    # basic structure
    
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
        if self.head is None:
            print('list is empty!')
            return
        temp = self.head
        while temp:
            print(temp.data, end = '->')
            temp = temp.next
        print('None')
        
    # Insertion
    
    def insert_at_start(self, data):
        newNode = Node(data)
       
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
       
        newNode.next = self.head
        self.head = newNode
       
    def insert_at_Kth(self, data, k):
        if k == 1:
            self.insert_at_start(data)
            return   # IMPORTANT

        newNode = Node(data)
        cur = self.head
    
        for i in range(k-2):
            if cur is None:
                print('position out of range')
                return
            cur = cur.next
    
        if cur is None:
            print('position out of range')
            return
    
        newNode.next = cur.next
        cur.next = newNode
    
        if newNode.next is None:
            self.tail = newNode
            
    # Deletion
    
    def delete_at_start(self):
        if self.head is None:
            print('linked list is empty!')
            return 
        
        self.head = self.head.next
        
    def delete_at_end(self):
        if self.tail is None:
            print('linked list is empty!')
        
        cur = self.head
        while cur.next.next:
            cur = cur.next
        self.tail = cur
        self.tail.next = None
    
    def delete_at_kth(self, k):
        
        cur = self.head
        
        for i in range(k-2):
            if cur is None:
                print('linked list out of range!')
                return
            
            cur = cur.next
        if cur is None:
            print('linked list out of range!')
            return
        
        cur.next = cur.next.next
        if cur.next is None:
            self.tail = cur
        
l = SinglyLL()
l.append(1)
l.append(2)
l.append(3)
l.append(4)

l.display()

l.insert_at_start(0)
l.display()
l.insert_at_Kth(3.5, 5)
l.display()           
l.insert_at_Kth(5.5, 8)
l.display()
l.insert_at_Kth(0.5, 1) 
l.display()

l.delete_at_start()
l.display()
l.delete_at_kth(3)
l.display()
l.delete_at_end()
l.display()          
