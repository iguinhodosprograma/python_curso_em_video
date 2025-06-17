from random import randint
import time
print("ESCOLHA UM DADO PARA ROLAR\n")
print("d4, d6, d10, d12, d20, d100")
dado = int(input("ESCREVA APENAS A NUMERAÇÃO DO DADO "))
segundo = 3
while segundo > 0:
    print("-"*33,segundo,"-"*33)
    time.sleep(1)
    segundo -= 1


print("""\n\n██████╗ ███████╗███████╗██╗   ██╗██╗  ████████╗ █████╗ ██████╗  ██████╗ 
██╔══██╗██╔════╝██╔════╝██║   ██║██║  ╚══██╔══╝██╔══██╗██╔══██╗██╔═══██╗
██████╔╝█████╗  ███████╗██║   ██║██║     ██║   ███████║██║  ██║██║   ██║
██╔══██╗██╔══╝  ╚════██║██║   ██║██║     ██║   ██╔══██║██║  ██║██║   ██║
██║  ██║███████╗███████║╚██████╔╝███████╗██║   ██║  ██║██████╔╝╚██████╔╝
╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝  ╚═╝╚═════╝  ╚═════╝ 
                                                                        """)
if dado == 4:
    dado = randint(1,4)
    print("="*33,dado,"="*33)

elif dado == 6:
    dado = randint(1,6)
    print("="*33,dado,"="*33)

elif dado == 10:
    dado = randint(1,10)
    print("="*33,dado,"="*33)
    
elif dado == 12:
    dado = randint(1,12)
    print("="*33,dado,"="*33)
    
elif dado == 20:
    dado = randint(1,20)
    print("="*33,dado,"="*33)
    
elif dado == 100:
    dado = randint(1,100)
    print("="*33,dado,"="*33)
