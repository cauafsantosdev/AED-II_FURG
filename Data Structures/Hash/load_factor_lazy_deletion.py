class HashTableOpenAddressing:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.chaves = [None] * tamanho
        self.valores = [None] * tamanho
        self.deletado = [False] * tamanho  # ← LAZY DELETION
        self.elementos = 0  # ← Para calcular LOAD FACTOR
    
    def load_factor(self):
        return self.elementos / self.tamanho
    
    def inserir(self, chave, valor):
        if self.load_factor() >= 0.7:  # ← VERIFICA LOAD FACTOR
            print(f"⚠️ Load Factor alto: {self.load_factor():.2f} - Performance degradada!")
        
        indice = chave % self.tamanho
        print(f"Inserindo {chave}:{valor} (Load Factor: {self.load_factor():.2f})")
        
        while self.chaves[indice] is not None and not self.deletado[indice]:
            if self.chaves[indice] == chave:
                self.valores[indice] = valor  # Atualiza
                print(f"Atualizado na posição {indice}")
                return
            indice = (indice + 1) % self.tamanho
        
        # Pode inserir (posição vazia OU deletada)
        if self.chaves[indice] is None:
            self.elementos += 1  # ← Só conta como novo se era None
        
        self.chaves[indice] = chave
        self.valores[indice] = valor
        self.deletado[indice] = False
        print(f"Inserido na posição {indice}")
    
    def buscar(self, chave):
        indice = chave % self.tamanho
        
        while self.chaves[indice] is not None:
            if self.chaves[indice] == chave and not self.deletado[indice]:
                return self.valores[indice]
            indice = (indice + 1) % self.tamanho
        return None
    
    def deletar(self, chave):
        indice = chave % self.tamanho
        
        while self.chaves[indice] is not None:
            if self.chaves[indice] == chave and not self.deletado[indice]:
                self.deletado[indice] = True  # ← LAZY DELETION
                self.elementos -= 1
                print(f"Chave {chave} marcada como deletada na posição {indice}")
                return True
            indice = (indice + 1) % self.tamanho
        return False
    
    def mostrar_estado(self):
        print(f"\nLoad Factor: {self.load_factor():.2f} ({self.elementos}/{self.tamanho})")
        for i in range(self.tamanho):
            if self.chaves[i] is not None:
                status = "DELETADO" if self.deletado[i] else "ATIVO"
                print(f"[{i}]: {self.chaves[i]} → {self.valores[i]} ({status})")
            else:
                print(f"[{i}]: [VAZIO]")

# Demonstração
print("=== DEMONSTRAÇÃO: LOAD FACTOR E LAZY DELETION ===")
hash_table = HashTableOpenAddressing(7)

# Inserindo elementos
print("\n--- INSERINDO ELEMENTOS ---")
hash_table.inserir(12, "João")
hash_table.inserir(19, "Maria") 
hash_table.inserir(26, "Pedro")
hash_table.inserir(33, "Ana")
hash_table.inserir(40, "Luis")
hash_table.mostrar_estado()

# Deletando João (lazy deletion)
print("\n--- DELETANDO JOÃO ---")
hash_table.deletar(12)
hash_table.mostrar_estado()

# Buscando Maria (deve funcionar mesmo com João deletado)
print("\n--- BUSCANDO MARIA ---")
resultado = hash_table.buscar(19)
print(f"Maria encontrada: {resultado}")

# Inserindo novo elemento na posição "deletada"
print("\n--- INSERINDO CARLOS NA POSIÇÃO DE JOÃO ---")
hash_table.inserir(47, "Carlos")  # 47 % 7 = 5 (mesma posição de João)
hash_table.mostrar_estado()

print("\n🎯 RESUMO:")
print("• Load Factor alto → performance ruim")
print("• Lazy deletion mantém a 'ponte' para outros elementos")
print("• Posições deletadas podem ser reutilizadas")
