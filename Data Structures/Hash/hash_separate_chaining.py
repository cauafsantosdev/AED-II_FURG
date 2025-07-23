class HashTableChaining:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        # Cada posição é uma lista vazia
        self.tabela = [[] for _ in range(tamanho)]
    
    def hash(self, chave):
        return chave % self.tamanho
    
    def inserir(self, chave, valor):
        indice = self.hash(chave)
        bucket = self.tabela[indice]  # Lista nessa posição
        
        # Verifica se a chave já existe na lista
        for i, (k, v) in enumerate(bucket):
            if k == chave:
                bucket[i] = (chave, valor)  # Atualiza valor
                return
        
        # Se não existe, adiciona na lista
        bucket.append((chave, valor))
        print(f"Inserido {chave}:{valor} no índice {indice}")
    
    def buscar(self, chave):
        indice = self.hash(chave)
        bucket = self.tabela[indice]
        
        # Busca na lista dessa posição
        for k, v in bucket:
            if k == chave:
                return v
        return None
    
    def __str__(self):
        resultado = ""
        for i, bucket in enumerate(self.tabela):
            if bucket:  # Se a lista não está vazia
                resultado += f"[{i}]: {bucket}\n"
            else:
                resultado += f"[{i}]: []\n"
        return resultado

# Teste prático
print("=== SEPARATE CHAINING ===")
hash_chain = HashTableChaining(7)

# Inserindo elementos que causam colisões
elementos = [15, 22, 8, 29, 36]  # Todos têm resto 1 quando divididos por 7
for elem in elementos:
    hash_chain.inserir(elem, f"Valor_{elem}")

print("\nEstado da tabela:")
print(hash_chain)

print(f"Buscar 22: {hash_chain.buscar(22)}")
print(f"Buscar 99: {hash_chain.buscar(99)}")
