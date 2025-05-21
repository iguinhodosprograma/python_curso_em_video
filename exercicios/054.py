menor = 0
maior = 0
for c in range (1,8):
    ano = int(input(f"Em que ano a {c}ª pessoa nasceu?"))
    idade = 2025 - ano
    if idade < 18:
        menor += 1
    else:
        maior += 1
print(f"Ao todo tivemos {maior} pessoas maiores de idade")
print(f"E tambem tivemos {menor} pessoas menores de idade")