ano_nascimento = int(input("Digite o ano de seu nascimento: "))
animais_chineses = ["Rato", "Boi", "Tigre", "Coelho", "Dragão", "Serpente", "Cavalo", "Cabra", "Macaco", "Galo", "Cachorro", "Porco"]
indice_animal = (ano_nascimento - 1900) % 12
signo_chines = animais_chineses[indice_animal]
print(f"Seu signo chinês é: {signo_chines}")