class HashTableChaining:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]
    
    def hash(self, chave):
        return chave % self.tamanho
    
    def inserir(self, chave, valor):
        indice = self.hash(chave)
        bucket = self.tabela[indice]
        
        # Verifica se a chave já existe na lista
        for i, (k, v) in enumerate(bucket):
            if k == chave:
                bucket[i] = (chave, valor)  # Atualiza valor
                return
        
        # Se não existe, adiciona na lista
        bucket.append((chave, valor))
        print(f"Inserido {chave}:{valor} no índice {indice}")
    
    def buscar(self, chave):
        print(f"\n=== BUSCANDO CHAVE {chave} ===")
        
        # Passo 1: Calcular o hash para saber qual posição/lista verificar
        indice = self.hash(chave)
        print(f"1. Hash de {chave} = {chave} % {self.tamanho} = {indice}")
        
        # Passo 2: Pegar a lista dessa posição
        bucket = self.tabela[indice]
        print(f"2. Lista na posição {indice}: {bucket}")
        
        # Passo 3: Percorrer a lista procurando a chave específica
        print(f"3. Procurando chave {chave} na lista:")
        for i, (k, v) in enumerate(bucket):
            print(f"   - Elemento {i}: chave={k}, valor={v}")
            if k == chave:
                print(f"   ✓ ENCONTROU! Chave {k} = {chave}")
                return v
            else:
                print(f"   ✗ Chave {k} ≠ {chave}, continua procurando...")
        
        print(f"   ✗ Chave {chave} NÃO encontrada na lista")
        return None
    
    def __str__(self):
        resultado = ""
        for i, bucket in enumerate(self.tabela):
            resultado += f"[{i}]: {bucket}\n"
        return resultado

# Teste detalhado
print("=== DEMONSTRAÇÃO: COMO ENCONTRAR VALOR NA LISTA ===")
hash_chain = HashTableChaining(7)

# Inserindo elementos que fazem hash para a mesma posição
print("Inserindo elementos que causam colisões:")
elementos = [15, 22, 8, 29]  # Todos fazem hash para posição 1 (resto da divisão por 7)
for elem in elementos:
    hash_chain.inserir(elem, f"Valor_{elem}")

print(f"\nEstado atual da tabela:")
print(hash_chain)

# Agora vamos buscar diferentes elementos para ver o processo
print("Agora vamos buscar elementos para ver como funciona:")

# Busca 1: Elemento que está no início da lista
resultado1 = hash_chain.buscar(15)
print(f"RESULTADO: {resultado1}")

# Busca 2: Elemento que está no meio da lista  
resultado2 = hash_chain.buscar(8)
print(f"RESULTADO: {resultado2}")

# Busca 3: Elemento que está no final da lista
resultado3 = hash_chain.buscar(29)
print(f"RESULTADO: {resultado3}")

# Busca 4: Elemento que NÃO existe
resultado4 = hash_chain.buscar(99)
print(f"RESULTADO: {resultado4}")
