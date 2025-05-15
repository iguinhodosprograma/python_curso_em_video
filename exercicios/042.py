l1 = int(input("lado 1: "))
l2 = int(input("lado 2: "))
l3 = int(input("lado 3: "))

if (l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2) == False:
    print("NÃO é possivel formar um triangulo")
else:
    if l1 == l2 == l3:
        print("O triangulo é EQUILATERO")
        
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print("O triangulo é ISOSCELES")
        
    else:
        print("O triangulo é ESCALENO")
