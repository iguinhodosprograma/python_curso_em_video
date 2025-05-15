f = str(input('Digite uma frase: ')).strip().upper()
print('A primeira letra A aparece na posicao {}'.format(f.find('A')+1))
print('A ultima letra A aparece na posicao {}'.format(f.rfind('A')+1))