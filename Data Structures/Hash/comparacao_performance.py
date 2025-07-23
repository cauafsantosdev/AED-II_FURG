import time
import random
from Tabela2 import Tabela

# Testando performance da sua classe Tabela vs dict Python (que usa hash)

def teste_performance():
    # Preparando dados
    dados = [(random.randint(1, 100000), f"Valor_{i}") for i in range(10000)]
    
    # Testando sua Tabela (busca linear)
    print("=== SUA TABELA (Busca Linear) ===")
    tabela = Tabela(15000)
    
    start = time.time()
    for chave, valor in dados:
        tabela.inserir(chave, valor)
    tempo_insercao_tabela = time.time() - start
    print(f"Inserção de 10.000 elementos: {tempo_insercao_tabela:.4f}s")
    
    # Testando buscas
    chaves_teste = [random.choice(dados)[0] for _ in range(1000)]
    start = time.time()
    for chave in chaves_teste:
        resultado = tabela.consultar(chave)
    tempo_busca_tabela = time.time() - start
    print(f"1.000 buscas: {tempo_busca_tabela:.4f}s")
    
    # Testando dict Python (usa hash table)
    print("\n=== DICT PYTHON (Hash Table) ===")
    dicionario = {}
    
    start = time.time()
    for chave, valor in dados:
        dicionario[chave] = valor
    tempo_insercao_dict = time.time() - start
    print(f"Inserção de 10.000 elementos: {tempo_insercao_dict:.4f}s")
    
    start = time.time()
    for chave in chaves_teste:
        resultado = dicionario.get(chave)
    tempo_busca_dict = time.time() - start
    print(f"1.000 buscas: {tempo_busca_dict:.4f}s")
    
    # Comparação
    print("\n=== COMPARAÇÃO ===")
    print(f"Hash é {tempo_insercao_tabela/tempo_insercao_dict:.1f}x mais rápido na inserção")
    print(f"Hash é {tempo_busca_tabela/tempo_busca_dict:.1f}x mais rápido na busca")

if __name__ == "__main__":
    teste_performance()
