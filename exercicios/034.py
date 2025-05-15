s = float(input("Quanto eh o seu salario? "))
if s <= 1250.00:
    aumento = (s * 0.15) + s
    print(f"Seu novo salario eh de {aumento}")
else: 
    aumento = (s * 0.10) + s
    print(f"Seu novo salario eh de {aumento}")