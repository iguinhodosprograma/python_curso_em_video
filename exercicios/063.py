print("-"*30)
print("Sequencia de Fibonacci")
print("-"*30)
termos = int(input("Quantos termos voce quer mostrar? "))
a, b = 0, 1
i = 0
while i != termos:
    print(a, end=" -> ")
    a, b = b, a + b
    i+=1
print("FIM")
    