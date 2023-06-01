#Desafio 039 Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistar.
#Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
#Pegar o ano do sistema importando o módulo date
from datetime import date
ano = date.today().year
nascimento = int(input('Qual o ano do seu nascimento? '))
idade = ano - nascimento
print('''Qual o seu sexo:
[1] Masculino
[2] Feminino''')
sexo = int(input('Opção: '))
#Verificação do sexo do usuário, caso seja masculino o programa fornece as informações do alistamento e caso contrário emite um alerta que o serviço militar é obrigatório apenas para homens.
if sexo == 1:
    if idade < 18:
        tempo = 18 - idade
        alistamento = ano + tempo #Calculando quantos anos faltam para o alistamento
        print('Você ainda vai se alistar ao serviço militar, faltam {} anos.'.format(tempo))
        print('O ano do seu alistamendo é {}.'.format(alistamento))
    elif idade == 18:
        print('Você está na idade do alistamento militar.')
    else:
        tempo = idade - 18
        alistamento = ano - tempo #Calculando o ano do alistamento
        print('Você já passou {} anos do tempo de alistamento.'.format(tempo))
        print('Você deveria ter se alistado no ano de {}.'.format(alistamento))
if sexo == 2:
    print('O alistamento militar só é obrigatório para o sexo masculino.')