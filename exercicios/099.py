from time import sleep
lst = []

def lin():
    print("-=" * 60)
    
    
def maior(*num):
    for p in range(len(num)):
        lst.append(num[p])
    print("Analisando os valores passados...")
    for n in range(len(lst)):
        print(f"{lst[n]}", end=" ", flush=True)
        sleep(0.2)
    print(f"\nForam informados {len(lst)} valores ao todo")
    lst.sort()
    print(f"O maior valor informado foi {lst[-1]}")
    for p in range(len(num)):
        lst.pop()
lin()
maior(2, 9, 4, 5, 7, 1)
lin()
maior(4, 7, 0)
lin()
maior(1, 2)
lin()
maior(6)
lin()
maior(0)

