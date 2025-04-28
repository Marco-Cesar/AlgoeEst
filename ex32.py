tabuada_numero=int(input("digite o numero da tabuada"))
numero_iniciao=int(input("digite o numero inicião"))
numero_fim=int(input("digite o numero final"))           
def tabuada_pesonalizada(base, inicio, fim):
    print(f"Tabuada do {base} de {inicio} a {fim}:")
    for j in range(inicio, fim + 1):
        print(f"{base} x {j} = {base * j}")
    print()

#Uso
tabuada_pesonalizada(tabuada_numero,numero_iniciao,numero_fim)
