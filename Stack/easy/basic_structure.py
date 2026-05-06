class tree():
    def __init__(self):
        self.node = []
        
    def push(self, value):
        self.node.append(value)
        
    def pop(self):
        if not self.is_empty():
            return self.node.pop()
        return 'underflow'
        
    def peek(self):
        if not self.is_empty():
            return self.node[-1]
        return None
        
    def is_empty(self):
        return len(self.node) == 0
        
s = tree()
s.push(45)
s.push(76)
s.push(98) 
print(s.pop())
print(s.peek())
print(s.pop())
print(s.is_empty())
print(s.peek())
print(s.pop())
print(s.peek())
print(s.pop())
print(s.is_empty())
