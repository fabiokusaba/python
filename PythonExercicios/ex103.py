#Desafio 103 Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


#Programa Principal
#Se eu passar a minha variável gol como sendo int caso eu não venha a digitar um valor o Python vai me alertar sobre um erro e ele não me deixa fazer isso, por isso vamos passar como string (str).
#Em seguida vamos fazer a verificação se a minha variável gol é numérico ou não, se for eu faço: que a minha variável gol é um inteiro de gol, se não for eu faço: que a minha variávle gol é 0
#Agora eu vou fazer com que se o nome do jogador tirando todos os espaços com strip() for vazio eu vou chamar a ficha() e passar que gols = gol, se não eu vou chamar de outro jeito sendo que aqui vou passar na ficha jogador e gol.
jogador = str(input('Nome do jogador: '))
gol = str(input('Gol(s) marcados: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jogador.strip() == '':
    ficha(gols=gol)
else:
    ficha(jogador,gol)