class ContiguousList:
    def __init__(self, m: int):
        self.max = m
        self.vector = [None] * self.max
        self.start = None
        self.end = None

    def empty(self):
        return self.start == None or self.end == None

    def size(self):
        if not self.empty():
            return self.end - self.start + 1
        return 0

    def value(self, pos: int):
        if 0 <= pos < self.size():
            return self.vector[self.start + pos]
        return None

    def position(self, value):
        for i in range(self.start, self.end + 1):
            if self.vector[i] == value:
                return i - self.start
        return None

    def insert(self, pos: int, value):
        if self.size() >= self.max or not (0 <= pos <= self.size()):
            return

        if self.start == None and self.end == None:
            self.start = 0
            self.end = 0
            self.vector[self.start] = value
            return

        insert_index = self.start + pos

        for i in range(self.end, insert_index - 1, -1):
            self.vector[i + 1] = self.vector[i]

        self.vector[insert_index] = value
        self.end += 1

    def remove(self, pos: int):
        if self.empty() or not (0 <= pos < self.size()):
            return

        remove_index = self.start + pos
        for i in range(remove_index, self.end):
            self.vector[i] = self.vector[i + 1]
        self.vector[self.end] = None
        self.end -= 1
        if self.end < self.start:
            self.start = None
            self.end = None

    def clear(self):
        self.vector = [None] * self.max
        self.start = None
        self.end = None


my_list = ContiguousList(5)

my_list.insert(0, "Produto A")
my_list.insert(1, "Produto B")
my_list.insert(1, "Produto C")
print("Após inserções:")
print(my_list.vector)

print("\nValor na posição 0:", my_list.value(0))
print("Valor na posição 1:", my_list.value(1))
print("Valor na posição 2:", my_list.value(2))

print("Valor na posição 3:", my_list.value(3))

print("\nPosição do 'Produto B':", my_list.position("Produto B"))
print("Posição de um produto inexistente:", my_list.position("Produto X"))

print("\nTamanho da lista:", my_list.size())

my_list.remove(1)
print("\nApós remoção do meio:")
print(my_list.vector)
print("Tamanho da lista:", my_list.size())

my_list.remove(1)
print("\nApós remoção do final:")
print(my_list.vector)
print("Tamanho da lista:", my_list.size())

my_list.remove(0)
print("\nApós remoção final:")
print(my_list.vector)
print("Tamanho da lista:", my_list.size())

my_list.insert(0, "Product D")
print("\nApós nova inserção:")
print(my_list.vector)

my_list.clear()
print("\nApós limpeza:")
print(my_list.vector)
print("Tamanho da lista:", my_list.size())
print("Lista vazia:", my_list.empty())