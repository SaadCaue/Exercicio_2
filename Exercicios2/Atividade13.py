def tentativa_raiz_quadrada(n):
    aproximacao = 0.001
    x = n

    while True:
        raiz_aproximadamente = 0.5 * (x + n / x)
        if abs(raiz_aproximadamente - x) < aproximacao:
            return raiz_aproximadamente
        x = raiz_aproximada

numero = int(input("Digite um número inteiro positivo: "))
raiz = raiz_quadrada(numero)
print(f"A raiz quadrada de {numero} com precisão de 0.001 é aproximadamente {raiz:.3f}")
