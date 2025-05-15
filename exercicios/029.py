km=int(input("Quantos km/h voce estava? "))
preco = (km - 80) * 7
if km <= 80:
    print("Voce estava na velocidade correta.")
else:
    print(f"Voce foi multado em um valor de R${preco}")
    