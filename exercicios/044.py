print("="*30, "LOJAS IGAO", "="*30)

compra = float(input("valor da compra: R$"))
formapag = int(input("""FORMAS DE PAGAMENTO
                     [ 1 ] À vista (dinheiro/cheque) --> 10% de desconto <--
                     [ 2 ] À vista (cartão) --> 5% de desconto <--
                     [ 3 ] Até 2x no cartao --> preco normal <--
                     [ 4 ] 3x ou mais no cartao --> 20% de juros <--
                     Sua escolha: """))

if formapag == 1:
    preco = compra - (compra * 0.10)
    print(f"O valor da compra foi R${preco}")
elif formapag == 2:
    preco = compra - (compra * 0.05)
    print(f"O valor da compra foi R${preco}")
elif formapag == 3:
    preco = compra
    print(f"O valor da compra foi R${preco}")
elif formapag == 4:
    preco = (compra * 0.20) + compra
    print(f"O valor da compra foi R${preco}")