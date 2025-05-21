print("-=-"*7)
print("LOJAS PEDROCA PAPAI")
print("-=-"*7)
total = totmil = 0
cont = menor = 0
barato = ""
while True:
    produto = str(input("Nome do produto: ")).capitalize()
    preco = float(input("Preço: R$"))
    total +=  preco
    cont += 1
    if preco > 1000:
        totmil += 1 
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    continuar = str(input("Quer continuar? [S/N]")).upper().strip()[0]
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]")).upper().strip()[0]
    if continuar == "N":
        break
print("{:-^40}".format(" FIM DO PROGRAMA "))
print(f"O total da compra foi de: R${total}")
print(f"Foram comprados {totmil} produtos de mais de R$1000,00")
print(f"O produto mais barato custa R${menor:.2f} e foi o {barato}")
        