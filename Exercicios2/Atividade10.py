numero = int(input("Digite um número: "))
quadrados = {i: i * i for i in range(1, numero + 1)}

print("Quadrados dos números:")
for i, quadrado in quadrados.items():
    print(f"{i}: {quadrado}")
