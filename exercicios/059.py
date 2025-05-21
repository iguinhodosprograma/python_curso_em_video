import time
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = int (input("""[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos numeros 
[ 5 ] Sair do programa
>>>>> Qual é a sua opçao? """))
while opcao != 5:
    if opcao == 1:
        s = n1 + n2
        print(f"A soma de {n1} + {n2} = {s}")
    elif opcao == 2:
        m = n1 * n2
        print(f"A multiplicaçao de {n1} X {n2} = {m}")
    elif opcao == 3:
        if n1 > n2:
            print(f"O maior numero é {n1}")
        elif n2 > n1:
            print(f"O maior numero é {n2}")
        else:
            print("Os numeros sao iguais")
    elif opcao == 4:
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    time.sleep(1)
    opcao = int (input("""-==-==-==-==-==-==-==-==-==-==-==-
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos numeros 
[ 5 ] Sair do programa
>>>>> Qual é a sua opçao? """))
print("Finalizando...")
time.sleep(1)
print("\nFim do programa. Volte sempre!")
