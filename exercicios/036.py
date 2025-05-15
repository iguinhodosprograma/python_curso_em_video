casa = float(input("Valor da casa R$"))
salario = float (input("Valor salario R$"))
anos = int(input("Em quantos anos deseja parcelar? "))
prestacao = casa/(anos * 12)
porcentagemsalario = salario * 0.30
print("para pagar uma casa de R${} em {} anos a prestacao sera de R${:.2f}".format(casa, anos, prestacao))
if prestacao > porcentagemsalario:
    print("Emprestimo NEGADO")

elif prestacao <= porcentagemsalario:
    print("Emprestimo AUTORIZADO")
    