import re
email_requerido = input("Digite seu endereço de e-mail: ")
padronizacao_email = r'^\S+@\S+\.\S+'
if re.match(padronizacao_email, email_requerido):
    print("O e-mail é válido.")
else:
    print("O e-mail não é válido.")
