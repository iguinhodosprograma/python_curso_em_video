times = ("Palmeiras","Flamengo",
"Cruzeiro","Red Bull Bragantino","Ceará",
"Bahia","Fluminense","Corinthians",
"Atlético-MG","Botafogo","São Paulo",
"Mirassol","Vasco da Gama","Internacional",
"Fortaleza","Santos","Grêmio",
"Vitória","Sport","Juventude")

print("-=-"*52)
print(f"Os 5 primeiros colocados são {times[0:6]}")
print("-=-"*52)
print(f"Os 4 ultimos colocados são {times[-4:]}")
print("-=-"*52)
print(f"Em ordem alfabetica fica {sorted(times)}")
print("-=-"*52)
print(f"O Bahia esta na {times.index("Bahia") + 1}ª posiçao ")
print("-=-"*52)