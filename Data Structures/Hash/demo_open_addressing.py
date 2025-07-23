class HashTableLinearProbing:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.chaves = [None] * tamanho
        self.valores = [None] * tamanho
    
    def hash(self, chave):
        return chave % self.tamanho
    
    def inserir(self, chave, valor):
        indice = self.hash(chave)
        indice_original = indice
        tentativas = 0
        
        print(f"\n=== INSERINDO {chave}:{valor} ===")
        print(f"Hash original de {chave} = {indice}")
        
        while self.chaves[indice] is not None:
            if self.chaves[indice] == chave:
                self.valores[indice] = valor  # Atualiza
                print(f"Chave {chave} já existe na posição {indice}, atualizando valor")
                return
            
            print(f"Posição {indice} ocupada por {self.chaves[indice]} → tentando próxima")
            indice = (indice + 1) % self.tamanho
            tentativas += 1
            
            if indice == indice_original:  # Tabela cheia
                print("ERRO: Tabela cheia!")
                return
        
        self.chaves[indice] = chave
        self.valores[indice] = valor
        print(f"✓ {chave} inserido na posição {indice} (deslocado {tentativas} posições)")
        self.mostrar_estado()
    
    def buscar(self, chave):
        print(f"\n=== BUSCANDO CHAVE {chave} ===")
        indice = self.hash(chave)
        indice_original = indice
        tentativas = 0
        
        print(f"Hash original de {chave} = {indice}")
        print("Seguindo o mesmo caminho da inserção:")
        
        while self.chaves[indice] is not None:
            print(f"Verificando posição {indice}: {self.chaves[indice]}")
            
            if self.chaves[indice] == chave:
                print(f"✓ ENCONTROU! {chave} está na posição {indice}")
                return self.valores[indice]
            
            print(f"  → {self.chaves[indice]} ≠ {chave}, continua procurando...")
            indice = (indice + 1) % self.tamanho
            tentativas += 1
            
            if indice == indice_original:
                break
        
        print(f"✗ Chave {chave} NÃO encontrada")
        return None
    
    def mostrar_estado(self):
        print("Estado atual da tabela:")
        for i in range(self.tamanho):
            if self.chaves[i] is not None:
                hash_original = self.chaves[i] % self.tamanho
                deslocamento = (i - hash_original) % self.tamanho
                print(f"  [{i}]: {self.chaves[i]} → {self.valores[i]} (hash original: {hash_original}, deslocado: {deslocamento})")
            else:
                print(f"  [{i}]: [VAZIO]")
        print()

# Demonstração prática
print("=== DEMONSTRAÇÃO: COMO O OPEN ADDRESSING 'LEMBRA' DAS COLISÕES ===")
hash_table = HashTableLinearProbing(7)

print("Vamos simular o exemplo dos apartamentos:")
print("João hash=5, Maria hash=5, Pedro hash=5")

# Inserindo elementos que fazem hash para posição 5
hash_table.inserir(12, "João")   # 12 % 7 = 5
hash_table.inserir(19, "Maria")  # 19 % 7 = 5 (colisão!)
hash_table.inserir(26, "Pedro")  # 26 % 7 = 5 (colisão!)

print("\n" + "="*50)
print("AGORA VAMOS BUSCAR PARA VER COMO ENCONTRA:")

# Buscando cada pessoa
resultado_joao = hash_table.buscar(12)
resultado_maria = hash_table.buscar(19)
resultado_pedro = hash_table.buscar(26)

print(f"\nResultados:")
print(f"João (12): {resultado_joao}")
print(f"Maria (19): {resultado_maria}")
print(f"Pedro (26): {resultado_pedro}")

print("\n" + "="*50)
print("IMPORTANTE: A tabela NÃO guarda que Maria 'deveria' estar na posição 5!")
print("Ela só sabe que Maria está na posição 6, e o algoritmo descobre isso")
print("refazendo o mesmo caminho: 5→6→encontrou!")
