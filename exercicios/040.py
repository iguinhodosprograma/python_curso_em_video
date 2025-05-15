n1 = float(input("primeira nota: "))
n2 = float(input("segunda nota: "))
media = (n1 + n2) / 2
if media >= 7:
    print("O aluno esta APROVADO")
elif 5 <= media < 7:
    print("O aluno esta em RECUPERAÇAO")
elif media < 5:
    print("O aluno esta REPROVADO")