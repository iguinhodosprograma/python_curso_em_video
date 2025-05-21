numeros = ("zero", "um", "dois", "tres", "quatro",
           "cinco", "seis", "sete", "oito", "nove",
           "dez", "onze", "doze", "treze", "quatorze",
           "quinze", "dezesseis", "dezessete", "dezoito",
           "dezenove", "vinte")
while True:
    posi = int(input("Digite uma posiçao para ser lida: "))
    if 0 <= posi <= 20:
        break
    print("Valor invalido, tente novamente")
print(f"Voce digitou o numero {numeros[posi]}")