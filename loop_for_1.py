# Usando o for com uma lista de números
numeros = [0, 18, 56, 77, 95]
for numero in numeros:
    print(f"Número: {numero}")

# Usando o for com uma lista de strings
frutas = ["Maçã", "Abacaxi","Melão", "Laranja"]
for fruta in frutas:
    print(f"Fruta: {fruta}")

# Usando o for com uma string
palavra = "Python"
for letra in palavra:
    print(letra)

# Usando else
numeros = [1, 2, 3, 10, 12]
for numero in numeros:
    print(f"Número:{numero}")
else:
    print("Acabou")

# Usando continue
for x in [1, 10, 20, 30, 40, 50]:
    if x == 30:
        continue
    print(x)