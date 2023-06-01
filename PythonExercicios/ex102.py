#Desafio 102 Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(num, show=False):
    """_summary_
    -> Função que calcula o fatorial de um número.
    Args:
        num: Número a ser calculado.
        show: (opcional) Mostrar ou não a conta.

    Returns:
        Retorna o valor de fatorial de num.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f
    
   
#Programa Principal     
print(fatorial(5))
help(fatorial)
