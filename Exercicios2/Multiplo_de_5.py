def multiplo_de_cinco(numero):
    numero = int(input("Digite um número por favor"))
    if numero % 5 == 0:
        return True
    else:
        return False
print(multiplo_de_cinco("numero"))