idade=int(input("insira sua idade"))
membro=input("voçe é membro")
aco_membro=input("voçe esta acompanhado por um membro")
if idade>18:
    if membro==True:
        print("liberado")
    elif aco_membro==True:
        print("pague metade da entrada")
    else:
        print("entrada no valor integral")
else:
    print("voce não tem idade nescessaria")