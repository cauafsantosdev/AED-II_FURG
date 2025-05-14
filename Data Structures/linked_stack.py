class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None

    def empty(self):
        if self.top == None:
            return True
        return False
    
    def insert(self, value):
        new = Node(value)

        if not self.empty():
            new.next = self.top
        
        self.top = new

    def remove(self):
        if not self.empty():
            self.top = self.top.next

    def search(self):
        return self.top.value
        
    def change(self, value):
        new = Node(value)
    
        if not self.empty():
            new.next = self.top.next
        
        self.top = new

    def reverse(self):
        aux = self.top
        aux_vector = [aux.value]

        while aux.next != None:
            aux = aux.next
            aux_vector.append(aux.value)

        self.destroy()

        for i in range(0, len(aux_vector)):
            self.insert(aux_vector[i])
        
    def compare(self, stack: "LinkedStack"):
        main_aux = self.top
        other_aux = stack.top
        
        while main_aux.next != None and other_aux.next != None:
            if main_aux.value != other_aux.value:
                return False
            main_aux = main_aux.next
            other_aux = other_aux.next
            
        return True
    
    def smallest(self): # If the Stack contains only integers and/or floats
        aux = self.top
        small = self.top.value

        while aux.next != None:
            aux = aux.next
            if aux.value < small:
                small = aux.value

        return small
    
    def print(self):
        aux = self.top

        while aux.next != None:
            print(aux.value)
            aux = aux.next

        print(aux.value)

    def destroy(self):
        while not self.empty():
            self.remove()

stack = LinkedStack()
stack.insert(1)
stack.insert(2)
stack.insert(3)
stack.insert(4)
stack.insert(5)
stack.insert(6)
stack.print()
print()
stack.reverse()
stack.print()


'''stack2 = LinkedStack()
stack2.insert(0)
stack2.insert(1)
stack2.insert(2)
stack2.insert(3)
stack2.insert(4)
stack2.insert(5)
stack2.print()
print()

print(stack.compare(stack2))
print(stack2.compare(stack))
print()

stack3 = LinkedStack()
stack3.insert(0)
stack3.insert(1)
stack3.insert(2)
stack3.insert(3)
stack3.insert(4)
stack3.print()
print()

print(stack.compare(stack3))
print()'''