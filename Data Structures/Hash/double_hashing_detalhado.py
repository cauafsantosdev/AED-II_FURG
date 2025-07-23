class HashTableDoubleHashing:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.chaves = [None] * tamanho
        self.valores = [None] * tamanho
    
    def hash1(self, chave):
        """Primeira função hash - determina posição inicial"""
        return chave % self.tamanho
    
    def hash2(self, chave):
        """Segunda função hash - determina o 'step' (tamanho do pulo)"""
        # Comum usar um número primo menor que o tamanho da tabela
        return 7 - (chave % 7)
    
    def inserir(self, chave, valor):
        # SEMPRE calcula ambos os hashes para a chave
        indice = self.hash1(chave)
        step = self.hash2(chave)
        
        print(f"\n=== INSERINDO {chave}:{valor} ===")
        print(f"Hash1({chave}) = {chave} % {self.tamanho} = {indice}")
        print(f"Hash2({chave}) = 7 - ({chave} % 7) = {step}")
        print(f"Padrão de sondagem: {indice}, {(indice + step) % self.tamanho}, {(indice + 2*step) % self.tamanho}, ...")
        
        tentativa = 0
        indice_original = indice
        
        while self.chaves[indice] is not None:
            if self.chaves[indice] == chave:
                self.valores[indice] = valor
                print(f"Chave {chave} já existe na posição {indice}, atualizando")
                return
            
            print(f"Posição {indice} ocupada por {self.chaves[indice]}")
            indice = (indice + step) % self.tamanho  # Próximo salto
            tentativa += 1
            print(f"Tentativa {tentativa}: indo para posição {indice}")
            
            if indice == indice_original:
                print("ERRO: Tabela cheia!")
                return
        
        self.chaves[indice] = chave
        self.valores[indice] = valor
        print(f"✓ Inserido na posição {indice}")
    
    def buscar(self, chave):
        # RECALCULA ambos os hashes (não estão guardados!)
        indice = self.hash1(chave)
        step = self.hash2(chave)
        
        print(f"\n=== BUSCANDO {chave} ===")
        print(f"Recalculando: Hash1({chave}) = {indice}, Hash2({chave}) = {step}")
        print("Seguindo o mesmo padrão da inserção:")
        
        indice_original = indice
        tentativa = 0
        
        while self.chaves[indice] is not None:
            print(f"Verificando posição {indice}: {self.chaves[indice]}")
            
            if self.chaves[indice] == chave:
                print(f"✓ ENCONTROU na posição {indice}!")
                return self.valores[indice]
            
            indice = (indice + step) % self.tamanho
            tentativa += 1
            print(f"Não é {chave}, pula para posição {indice}")
            
            if indice == indice_original:
                break
        
        print(f"✗ {chave} não encontrado")
        return None
    
    def mostrar_detalhes(self):
        print("\n=== ESTADO DA TABELA ===")
        for i in range(self.tamanho):
            if self.chaves[i] is not None:
                hash1_calc = self.hash1(self.chaves[i])
                hash2_calc = self.hash2(self.chaves[i])
                deslocamento = (i - hash1_calc) // hash2_calc if hash2_calc != 0 else 0
                print(f"[{i}]: {self.chaves[i]} → {self.valores[i]} (hash1={hash1_calc}, hash2={hash2_calc}, pulos={deslocamento})")
            else:
                print(f"[{i}]: [VAZIO]")

# Demonstração
print("=== DEMONSTRAÇÃO: DOUBLE HASHING NÃO GUARDA OS HASHES ===")
hash_table = HashTableDoubleHashing(11)

# Inserindo elementos
elementos = [10, 21, 32]  # Todos fazem hash1 para posição 10
for elem in elementos:
    hash_table.inserir(elem, f"Valor_{elem}")

hash_table.mostrar_detalhes()

# Buscando para mostrar que recalcula
hash_table.buscar(21)
hash_table.buscar(32)

print("\n" + "="*60)
print("IMPORTANTE:")
print("• O double hashing NÃO guarda os valores hash2 em lugar nenhum!")
print("• A cada busca, hash1 e hash2 são RECALCULADOS")
print("• É isso que garante que o algoritmo segue o mesmo padrão")
print("• Por isso as funções hash devem ser DETERMINÍSTICAS")
print("  (mesma entrada → mesma saída sempre)")
