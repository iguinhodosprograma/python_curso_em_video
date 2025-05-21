print(">>>Digite um numero negativo caso queira sair<<<")
i = 0
t = 0
while True:
    n = int(input("Quer ver a tabuada de qual numero? "))
    if n < 0:
        break
    while i < 10:
        i += 1
        t = i * n
        print(f"{n} X {i} = {t}")
    i -= 10
    print("="*40)
print("="*40)
print("PROGRAMA DE TABUADA ENCERRADO.")
print("Volte sempre!")
print("="*40)