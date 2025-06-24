from random import randint
from time import sleep
lst = []

def sorteia():
    """-> Sorteia valores de 1 até 10 e coloca eles em uma lista, mostrando um numero por vez na tela
    """
    
    n = 0
    print(f"Sorteando os valores da lista:", end=" ")
    for p in range(5):
        n = randint(1, 10)
        lst.append(n)
        print(lst[p], end=" ", flush=True)
        sleep(0.3)
    print("PRONTO!")
    
    
def somapar():
    soma = 0
    for p in range(len(lst)):
        if lst[p] % 2 == 0:
            soma += lst[p]
    print(f"Somando os valores pares de {lst}, temos {soma}")
    
    
sorteia()
somapar() 