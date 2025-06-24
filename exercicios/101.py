def voto(nacs=1):
    from datetime import datetime
    idade = datetime.now().year - nasc
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA"
    elif idade >= 16 and idade < 18:
        return f"Com {idade} anos: VOTO OPCIONAL"
    elif idade >= 18:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"

nasc = int(input("Ano de Nascimento: "))

print(voto(nasc))

