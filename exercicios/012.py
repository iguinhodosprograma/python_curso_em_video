preco=float(input("Quanto custa o produto? "))
desconto = preco - (preco * 0.05)
print("O preco final do produto é: R${:.2f}".format(desconto))