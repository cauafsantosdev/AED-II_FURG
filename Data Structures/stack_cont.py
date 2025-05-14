class Stack:
    def __init__(self, size: int):
        self.vector = [None] * size
        self.size = size - 1
        self.base = 0
        self.top = self.base - 1
    
    def insert(self, value):
        if self.top < self.size:
            self.top += 1
            self.vector[self.top] = value

    def remove(self):
        if self.top <= self.size:
            self.vector[self.top] = None
            self.top -= 1

    def search(self):
        if self.top >= self.base:
            return self.vector[self.top]
        
    def change(self, value):
        if self.top >= self.base:
            self.vector[self.top] = value

    def reverse(self):
        aux_stack = Stack(self.size + 1)

        for i in range(self.top, self.base-1, -1):
            if self.vector[i] != None:
                aux_stack.insert(self.vector[i])

        self.vector = aux_stack.vector

    def compare(self, stack: "Stack"):
        if self.size != stack.size or self.top != stack.top:
            return False
        
        for i in range(self.top + 1):
            if self.vector[i] != stack.vector[i]:
                return False
            
        return True
    
    def smallest(self): # If the Stack contains only integers and/or floats
        small = self.vector[self.base]

        for i in range(self.base + 1, self.top + 1):
            if self.vector[i] < small:
                small = self.vector[i]

        return small
    
    def print(self):
        for i in reversed(self.vector):
            print(i)

    def destroy(self):
        size = len(self.vector)
        self.vector = [None] * size
        self.top = self.base - 1


stack = Stack(10)
stack.insert(0)
stack.insert(1)
stack.insert(2)
stack.insert(3)
stack.insert(4)
stack.insert(5)
stack.print()
print()
print(stack.smallest())
print()
stack.reverse()
stack.print()
print()
print(stack.smallest())
print()
