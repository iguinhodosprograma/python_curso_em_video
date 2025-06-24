def notas(*n, sit=False):
    """
    -> Função para análise de notas e situação de alunos
    param n: uma ou mais notas de alunos
    param sit (opcional): indica se deve ou não adicionar a situação do aluno
    return: dicionário com várias informações sobre a situação do aluno
    """
    r = {}
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["media"] = sum(n)/len(n)
    if sit:
        if r["media"] < 7:
            r["situacao"] = "RUIM"
        elif r["media"] > 8:
            r["situacao"] = "BOM"
        elif r["media"] >= 7:
            r["situacao"] = "RAZOÁVEL"
    return r


resp = notas(8.5, 2.5, 9, 8.5, sit=True)
print(resp)
