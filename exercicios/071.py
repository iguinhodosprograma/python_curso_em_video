print("BEM VINDO\n")
valor = int(input("Qual valor voce quer sacar? "))
c50 = 0
c20 = 0
c10 = 0 
c1 = 0

while valor >= 50:
    valor -= 50
    c50 += 1
    
while valor >= 20:
    valor -= 20
    c20 += 1
    
while valor >= 10:
    valor -= 10
    c10 += 1
    
while valor >= 1:
    valor -= 1
    c1 += 1
    
if c50 > 0:
    print(f"Total de {c50} cédulas de R$50")
if c20 > 0:
    print(f"Total de {c20} cédulas de R$20")
if c10 > 0:
    print(f"Total de {c10} cédulas de R$10")
if c1 > 0:
    print(f"Total de {c1} cédulas de R$1")
