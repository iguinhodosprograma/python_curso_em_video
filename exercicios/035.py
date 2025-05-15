a = float(input("Digite o comprimento de uma reta: "))
b = float(input("Digite o comprimento de outra reta: "))
c = float(input("Digite o comprimento de outra reta: "))

if a+b>c and a+c>b and b+c>a:
    print("Eh possivel formar um triangulo com esses valores")
else:
    print("Nao eh possivel formar um triangulo com esses valores")

