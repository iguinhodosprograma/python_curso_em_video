altura = float(input("Altura em metros: "))
peso = float(input("Pedro em kg: "))
imc = peso / altura**2
print(f"O IMC dessa pesoa é {imc}")

if imc < 18.5:
    print("Voce esta ABAIXO DO PESO")
elif 18.5 <= imc < 25:
    print("Voce esta no PESO IDEAL")
elif 25 <= imc < 30:
    print("Voce esta em SOBREPESO")
elif 30 <= imc < 40:
    print("Voce esta em OBESIDADE")
else: 
    print("Voce esta em OBESIDADE MORBIDA")
