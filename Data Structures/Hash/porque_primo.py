print("=== POR QUE NÚMERO PRIMO NO DOUBLE HASHING ===\n")

def mostrar_ciclo(tamanho_tabela, step):
    print(f"Tabela tamanho {tamanho_tabela}, step = {step}")
    posicoes_visitadas = []
    posicao = 0
    
    while True:
        if posicao in posicoes_visitadas:
            print(f"Posições visitadas: {posicoes_visitadas}")
            print(f"Voltou para posição {posicao} - CICLO COMPLETO!")
            print(f"Total de posições únicas visitadas: {len(posicoes_visitadas)}/{tamanho_tabela}")
            if len(posicoes_visitadas) == tamanho_tabela:
                print("✅ VISITOU TODAS - BOM!")
            else:
                print("❌ NÃO VISITOU TODAS - PROBLEMA!")
            break
        
        posicoes_visitadas.append(posicao)
        posicao = (posicao + step) % tamanho_tabela
    print()

print("--- CASO RUIM: Tamanho 10 (não primo), Step 4 ---")
mostrar_ciclo(10, 4)

print("--- CASO RUIM: Tamanho 10 (não primo), Step 6 ---") 
mostrar_ciclo(10, 6)

print("--- CASO BOM: Tamanho 11 (primo), Step 4 ---")
mostrar_ciclo(11, 4)

print("--- CASO BOM: Tamanho 11 (primo), Step 7 ---")
mostrar_ciclo(11, 7)

print("🎯 REGRA DE OURO:")
print("Se o tamanho da tabela é PRIMO, qualquer step de 1 até (tamanho-1)")
print("vai visitar TODAS as posições!")
print()
print("Por isso usamos:")
print("• Tamanho da tabela: número primo (ex: 11, 13, 17...)")
print("• hash2(chave) = primo_menor - (chave % primo_menor)")
print("• Isso garante que step nunca seja 0 e sempre visite tudo!")
