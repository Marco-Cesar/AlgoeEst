nota1=int(input("digite uma nota"))
nota2=int(input("digite uma nota"))
nota3=int(input("digite uma nota"))
nota=nota1+nota2+nota3/3
if nota>=7 and nota<=8:
    print("o aluno está aprovado")
elif nota<=7 and nota>=5:
    print("o aluno está em recuperação")
else:  
    nota<5 
    print("o aluno está reprovado")