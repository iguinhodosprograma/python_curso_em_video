import moeda

p = float(input("Digite o preco: R$"))

print(f"A metade de R${p} é R${moeda.metade(p)}")
print(f"O dobro de R${p} é R${moeda.dobro(p)}")
print(f"Aumentando em 10%, temos R${moeda.aumentar(p, 10)}")
print(f"Diminuindo em 10%, temos R${moeda.diminuir(p, 10)}")