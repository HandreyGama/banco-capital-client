def verificador_cpf(cpf: str):
    soma = 0
    soma2 = 0
    peso1 = range(10, 2 - 1, -1)
    peso2 = range(11, 2 - 1, -1)
    cpf = cpf.replace(".", "").replace("-", "")
    for i, e in zip(cpf, peso1):
        m = int(i) * e
        soma += m
    p1 = (soma * 10) % 11
    if p1 == 10:
        p1 = 0
    for i, e in zip(cpf, peso2):
        m2 = int(i) * e
        soma2 += m2
    p2 = (soma2 * 10) % 11
    if p2 >= 10:
        p1 = 0
    if (cpf[-2] == str(p1)) and cpf[-1] == str(p2):
        return True
    else:
        return False
