#Desafio 101 Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
#Voto obrigatório acima de 18 anos.
#Voto opcional acima de 65 anos.
#Veja que como eu só vou utilizar date dentro da minha função eu posso simplesmente importar a biblioteca datetime e usar date() dentro da minha função mesmo, e isso nós chamamos de escopo de importação. E neste caso quando eu importo uma biblioteca para dentro de uma função o import só funciona dentro dela e isso economiza memória.

def voto(nasc):
    from datetime import date
    ano = date.today().year
    idade = ano - nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    

#Programa Principal
nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))