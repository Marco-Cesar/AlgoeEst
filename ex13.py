nome = input("insira seu nome:")
idade = int(input("insira sua idade:"))
turma = input("insira sua turma:")

if idade >=6:
    print(f"Aluno cadastrado com sucesso {nome}, {idade} anos, turma {turma}")
else:
    print("A criança ainda nao tem idade suficiente")