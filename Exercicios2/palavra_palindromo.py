def palavra_verificada_palindromo(letras):
    palavra_normal = input("Digite por gentileza uma palavra:" )
    palavra_em_palin = palavra_normal[: -1]
    if palavra_normal.lower() == palavra_em_palin:
        return " É um palíndromo"
    else:
        return "Não é um palíndromo"
print( palavra_verificada_palindromo("letras"))