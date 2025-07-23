class HashTableDoubleHashing:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.chaves = [None] * tamanho
        self.valores = [None] * tamanho
    
    def hash1(self, chave):
        return chave % self.tamanho
    
    def hash2(self, chave):
        # Segunda função hash (deve ser relativamente primo com tamanho)
        return 7 - (chave % 7)
    
    def inserir(self, chave, valor):
        indice = self.hash1(chave)
        step = self.hash2(chave)
        indice_original = indice
        tentativas = 0
        
        print(f"Tentando inserir {chave}:{valor}")
        print(f"Hash1: {indice}, Hash2: {step}")
        
        while self.chaves[indice] is not None:
            if self.chaves[indice] == chave:
                self.valores[indice] = valor
                print(f"Atualizado na posição {indice}")
                return
            
            indice = (indice + step) % self.tamanho
            tentativas += 1
            print(f"Colisão! Tentativa {tentativas}: posição {indice}")
            
            if indice == indice_original:
                print("ERRO: Tabela cheia!")
                return
        
        self.chaves[indice] = chave
        self.valores[indice] = valor
        print(f"Inserido na posição {indice}\n")
    
    def __str__(self):
        resultado = ""
        for i in range(self.tamanho):
            if self.chaves[i] is not None:
                resultado += f"[{i}]: {self.chaves[i]} → {self.valores[i]}\n"
            else:
                resultado += f"[{i}]: [VAZIO]\n"
        return resultado

# Teste prático
print("=== DOUBLE HASHING ===")
hash_double = HashTableDoubleHashing(11)

elementos = [10, 21, 32, 43]
for elem in elementos:
    hash_double.inserir(elem, f"Valor_{elem}")

print("Estado final da tabela:")
print(hash_double)
