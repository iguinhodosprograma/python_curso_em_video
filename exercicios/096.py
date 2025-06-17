def area(larg, comp):
    a = 0
    a = larg * comp
    print(f"A área de um terreno de {larg}X{comp} é de {a}m².")
def titulo(msg):
    print(f"\n{msg}")
    print("-"*20)
    
    
larg = float(input("LARGURA (m): "))
comp = float(input("COMPRIMENTO (m): "))

titulo("Controle de Terrenos")
area(larg, comp)
