ano = int(input("Qual ano voce esta? "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} NÃO é bissexto.')