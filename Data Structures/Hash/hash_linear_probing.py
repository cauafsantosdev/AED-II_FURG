class HashTableLinearProbing:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.chaves = [None] * tamanho
        self.valores = [None] * tamanho
        self.deletado = [False] * tamanho  # Para lazy deletion
    
    def hash(self, chave):
        return chave % self.tamanho
    
    def inserir(self, chave, valor):
        indice = self.hash(chave)
        indice_original = indice
        tentativas = 0
        
        print(f"Tentando inserir {chave}:{valor}")
        print(f"Hash inicial: {indice}")
        
        while self.chaves[indice] is not None and not self.deletado[indice]:
            if self.chaves[indice] == chave:
                self.valores[indice] = valor  # Atualiza
                print(f"Atualizado na posição {indice}")
                return
            
            # Linear probing: próxima posição
            indice = (indice + 1) % self.tamanho
            tentativas += 1
            print(f"Colisão! Tentativa {tentativas}: posição {indice}")
            
            if indice == indice_original:  # Tabela cheia
                print("ERRO: Tabela cheia!")
                return
        
        self.chaves[indice] = chave
        self.valores[indice] = valor
        self.deletado[indice] = False
        print(f"Inserido na posição {indice}\n")
    
    def buscar(self, chave):
        indice = self.hash(chave)
        indice_original = indice
        
        while self.chaves[indice] is not None:
            if self.chaves[indice] == chave and not self.deletado[indice]:
                return self.valores[indice]
            indice = (indice + 1) % self.tamanho
            if indice == indice_original:
                break
        return None
    
    def __str__(self):
        resultado = ""
        for i in range(self.tamanho):
            if self.chaves[i] is not None and not self.deletado[i]:
                resultado += f"[{i}]: {self.chaves[i]} → {self.valores[i]}\n"
            else:
                resultado += f"[{i}]: [VAZIO]\n"
        return resultado

# Teste prático
print("=== LINEAR PROBING ===")
hash_linear = HashTableLinearProbing(7)

# Inserindo elementos que causam colisões
elementos = [15, 22, 8, 29]  # Todos fazem hash para posição 1
for elem in elementos:
    hash_linear.inserir(elem, f"Valor_{elem}")

print("Estado final da tabela:")
print(hash_linear)

print(f"Buscar 22: {hash_linear.buscar(22)}")
print(f"Buscar 8: {hash_linear.buscar(8)}")
