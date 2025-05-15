km=int(input("Qual é a distancia em km da viagem? "))
if km <=200:
    passagem = km * 0.5
    print(f"A viagem custou {passagem}")
else:
    passagem = km *0.45
    print(f"A viagem custou {passagem}")