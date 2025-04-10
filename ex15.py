print("vericação bancária")
saldo=float(input("insira o saldo da conta"))
if saldo !=0:
    atividade_da_conta=True
else:
    atividade_da_conta=False
print("conta ativa") if atividade_da_conta==True else print("conta inativa")