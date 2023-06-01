#Desafio 091 Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
#Para eu colocar em ordem vou precisar criar um outro dicionário e vou chamá-lo de ranking
#Depois de ter formatado a visualização com for vou passar o meu ranking e ele vai receber o método sorted() e esse método não ordena no original ele precisa que seja jogado em outro dicionário.
#E agora eu preciso passar para dentro do meu sorted() aquilo que eu quero ordenar, quero ordenar o meu dicionário jogadas.items() e eu quero ordenar da seguinte forma: na posição 0 seria a chave e o valor na posição 1 e pra isso vou precisar de uma função chamada itemgetter() e para eu utilizá-la eu preciso importá-la de operator.
#Agora basta eu passar que a minha key=itemgetter(1) porque se for na parte 0 ele vai botar em ordem de chave e se for parte 1 ele vai botar em ordem de valor.
#E para finalizar como queremos que o nosso ranking seja do maior para o menor basta agora utilizarmos reverse=True
#Perceba que o retorno do nosso ranking é tratado como uma lista então agora para formatarmos sua exibição devemos também tratá-lo como uma lista.
#E por conta disso quando vamos tratá-lo não vamos utilizar mais o .items() agora vamos utilizar enumerate().
from random import randint
from time import sleep
from operator import itemgetter
jogadas = {'jogador1': randint(1, 6), 'jogador2': randint(1,6), 'jogador3': randint(1,6), 'jogador4': randint(1,6)}
ranking = dict()
print('SORTEANDO...')
for k, v in jogadas.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogadas.items(), key=itemgetter(1),reverse=True) #Ordenando do maior para o menor
print('RANKING DE JOGADORES')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}') #i simboliza nosso índice e vai contar 1º, 2º, 3º, 4º lugar
                                              #v simboliza o nosso valor e como este está dentro de uma tupla passamos os índices 0 para jogador e 1 para o valor tirado no dado.
    sleep(1)
print('FIM DE JOGO!')