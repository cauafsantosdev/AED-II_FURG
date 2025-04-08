def multiplicacao(a: str, b: str):
    shift_a = 1
    total = 0

    for i in a[::-1]:
        mid = 0
        shift_b = 1

        for j in b[::-1]:
            mid += (int(i) * shift_a) * (int(j) * shift_b)
            shift_b *= 10
        
        total += mid
        shift_a *= 10

    return total

a = input("Informe o primeiro número: ")
b = input("Informe o primeiro número: ")

resultado = multiplicacao(a, b)

print(resultado)
