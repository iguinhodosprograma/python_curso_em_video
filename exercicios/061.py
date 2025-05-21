primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
i = 0

while i != 10:
    print(f"{primeiro}", end=" -> ")
    primeiro += razao
    i +=1
print("FIM")