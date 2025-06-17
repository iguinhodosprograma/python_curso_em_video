situacao = ""
boletim = {}
boletim["nome"] = input("Nome: ")
boletim["media"] = float(input(f"Média de {boletim["nome"]}: "))

print("=-"*30)

if boletim["media"] <= 5:
    situacao = "reprovado"
elif boletim["media"] < 7:
    situacao = "recuperação"
elif boletim["media"] >= 7:
    situacao = "aprovado"
    
boletim["situacao"] = situacao

for k, v in boletim.items():
    print(f" - {k} é igual a {v}")

