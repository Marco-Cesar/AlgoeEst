senha=int(input("insira sua senha no minimo 8 caracteres:"))
print(len(senha))
if senha>=8:
    input("senha corretos")
elif senha<8:
    input("senha incorretos")
else:
    input("aceso negado")