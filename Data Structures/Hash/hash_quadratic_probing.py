class HashTableQuadraticProbing:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.chaves = [None] * tamanho
        self.valores = [None] * tamanho
    
    def hash(self, chave):
        return chave % self.tamanho
    
    def inserir(self, chave, valor):
        indice_original = self.hash(chave)
        i = 0
        
        print(f"Tentando inserir {chave}:{valor}")
        print(f"Hash inicial: {indice_original}")
        
        while i < self.tamanho:
            # Sondagem quadrática: h(k) + i²
            indice = (indice_original + i*i) % self.tamanho
            
            if self.chaves[indice] is None:
                self.chaves[indice] = chave
                self.valores[indice] = valor
                print(f"Inserido na posição {indice} (tentativa {i})\n")
                return
            elif self.chaves[indice] == chave:
                self.valores[indice] = valor  # Atualiza
                print(f"Atualizado na posição {indice}")
                return
            
            print(f"Colisão! Tentativa {i}: posição {indice}")
            i += 1
        
        print("ERRO: Não foi possível inserir!\n")
    
    def buscar(self, chave):
        indice_original = self.hash(chave)
        i = 0
        
        while i < self.tamanho:
            indice = (indice_original + i*i) % self.tamanho
            
            if self.chaves[indice] is None:
                return None
            elif self.chaves[indice] == chave:
                return self.valores[indice]
            
            i += 1
        return None
    
    def __str__(self):
        resultado = ""
        for i in range(self.tamanho):
            if self.chaves[i] is not None:
                resultado += f"[{i}]: {self.chaves[i]} → {self.valores[i]}\n"
            else:
                resultado += f"[{i}]: [VAZIO]\n"
        return resultado

# Teste prático
print("=== QUADRATIC PROBING ===")
hash_quad = HashTableQuadraticProbing(11)  # Tamanho primo

# Inserindo elementos que causam colisões
elementos = [10, 21, 32, 43]  # Todos fazem hash para posição 10%11 = 10, 21%11 = 10, etc.
for elem in elementos:
    hash_quad.inserir(elem, f"Valor_{elem}")

print("Estado final da tabela:")
print(hash_quad)
