import random
nome1=str(input("primeiro aluno: "))
nome2=str(input("segundo aluno: "))
nome3=str(input("terceiro aluno: "))
nome4=str(input("quarto aluno: "))
lista = [nome1,nome2,nome3,nome4]

print(f"O aludo escolhido foi: {random.choice(lista)}")