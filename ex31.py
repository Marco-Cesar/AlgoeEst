tabuada_numero=int(input("digite o numero"))
def tabuada(numero):
    print(f"Tabuada do{numero}:")
    for i in range(1,11):
        print(f"{numero} x {1} = {numero * i}")

tabuada(tabuada_numero)