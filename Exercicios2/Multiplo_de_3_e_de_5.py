def multiplo_de_cinco_e_de_tres(numero):
    numero= int(input("Digite um número, por gentileza: "))
    if numero % 5 == 0:
        return True
    if numero % 3 == 0:
            return True
    else:
            return False
print(multiplo_de_cinco_e_de_tres("numero"))