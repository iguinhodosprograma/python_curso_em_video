n=int(input("Digite um numero: "))
cores = {"azul":"\033[34m", "verde":"\033[32m", "amarelo":"\033[33m", "limpa":"\033[m"}

print(f"dobro = {cores["azul"]}{n*2}{cores["limpa"]}, triplo = {cores["verde"]}{n*3}{cores["limpa"]}, raiz quadrada = {cores["amarelo"]}{n**(1/2)}{cores["limpa"]}")