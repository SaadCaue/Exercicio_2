def prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

Numero = int(input(" Digite um número inteiro: "))

print(f"Os divisores primos de {Numero}:")
for i in range(1, Numero + 1):
    if Numero % i == 0 and prime(i):
        print(i)
