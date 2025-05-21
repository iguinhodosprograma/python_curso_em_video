from random import randint
print("Sou seu computador...")
print("Estou pensando em um numero de 0 até 10, sera que voce consegue adivinhar?")
pessoa = int(input("Qual é o seu palpite? "))
tentativa = 0
computador = randint(1,10)
while pessoa != computador:
    if computador > pessoa:
        print("Mais... tente mais uma vez.")
        pessoa = int(input("Qual é o seu palpite? "))
    elif computador < pessoa:
        print("Menos... Tente mais uma vez.")
        pessoa = int(input("Qual é o seu palpite? "))
    tentativa += 1
print(f"Acertou com {tentativa + 1} tentativas")