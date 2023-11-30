def palindromo(palavras):
    palavra = palavra.replace(" ", "").lower()
    return palavra == palavra[::-1]

o_palindromo = input("Digite uma palavra: ")

if palindromo("palavras"):
    print(f"{o_palindromo} é um palíndromo!")
else:
    print(f"{o_palindromo} não é um palíndromo.")