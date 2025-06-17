lista = []
for cont in range(0,5):
    lista.append((input(f"Digite um valor para a posiçao {cont}: ")))
    cont+=1

maior = max(lista)
menor = min(lista)
print(f"Voce digitou os valores{lista}")
    
print(f"O maior valor digitado foi {maior} nas posiçoes",end=' ')

for c,v in enumerate(lista):
    if v == maior:
        print(f"{c}...",end="")
        
print(f"\nO menor valor digitado foi {menor} nas posiçoes",end=" ")

for c,v in enumerate(lista):
    if v == menor:
        print(f"{c}...",end="")