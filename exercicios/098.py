from time import sleep

def lin():
    print("-="*30)
    
    
def contador(ini, fim, indice):
    while ini <= fim:
        print(ini, end=" ", flush=True)
        ini = ini + abs(indice)
        sleep(0.2)
    print("FIM!")
    
    
def contador_reverso(ini, fim, indice):
    while ini >= fim:
        print(ini, end=" ", flush=True)
        ini = ini - abs(indice)
        sleep(0.2)
    print("FIM!")
    
    
lin()
print("Contagem de 1 até 10 de 1 em 1")
contador(1, 10, 1)
lin()
print("Contagem de 10 até 0 de 2 em 2")
contador_reverso(10, 0, 2)
lin()

print("Agora é sua vez de personalizar a contagem!")
ini = int(input("Início: "))
fim = int(input("FIm: "))
indice = int(input("Passo: "))
lin()

contador(ini, fim, indice)

contador_reverso(ini, fim, indice)