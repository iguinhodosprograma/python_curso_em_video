sexo = input("Digite seu sexo [M/S]: ").strip().upper()[0]

while sexo not in "MS":
    sexo = input("Dados inválidos. Por favor, informe seu sexo: ").strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso")