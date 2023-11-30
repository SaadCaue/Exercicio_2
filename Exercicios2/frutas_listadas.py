frutas  = []
while True:
    fruta = input("Digite as frutas que deseje comprar, quando terminar, digite 'sair' para finalizar: ")
    if fruta.lower() == 'sair':
        break
    frutas.append(fruta)
print("Lista de frutas que deseja comprar: ")
for fruta in frutas:
    print(fruta)