def fatorial(n):
    f = 1 #fator de multiplicação se eu iniciar com zero qualquer número multiplicado por zero dá zero, então o fator nulo da multiplicação é um.
    for c in range(1, n+1):
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3