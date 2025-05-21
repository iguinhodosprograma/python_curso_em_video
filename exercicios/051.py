primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
fim = primeiro + (10 - 1) * razao
for c in range(primeiro, fim + razao, +razao):
    print(c, end = " -> ")
print("Acabou")