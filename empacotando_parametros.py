# Empacotamento de parâmetros
lista = [10, 20, True]

def soma(valor1, valor2, imprime = False):
    resultado = valor1 + valor2
    if imprime:
        print(f"Soma: {resultado}")
    return resultado

soma(lista[0], lista[1], True)
soma(*lista) # O asterisco indica que estamos desempacotando a lista

