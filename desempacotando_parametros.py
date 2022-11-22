# Desempacotamento de parâmetros
def soma(imprime, *valores):
    total = 0
    for valor in valores:
        total += valor
    if imprime:
        print(f"Soma: {total}")
    return total

soma(True, 10, 20, 30, 78)
soma(False, 10, 50)

