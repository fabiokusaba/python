#Desafio 093 Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
aproveitamento = dict()
gols = list()
aproveitamento['nome'] = str(input('Nome: '))
partidas = int(input(f'Quantas partidas o jogador {aproveitamento["nome"]} jogou? '))
for c in range(1, partidas + 1):
    gols.append(int(input(f'Quantos gols na {c}º partida? ')))
aproveitamento['gols_marcados'] = gols[:] #Fazendo uma cópia da minha lista gols para dentro do meu dicionário.
aproveitamento['total_gols'] = sum(aproveitamento['gols_marcados']) #Fazendo a soma dos gols marcados.
print('-=' * 30)
print(aproveitamento)
print('-=' * 30)
for k, v in aproveitamento.items(): #Trabalhando com dicionário.
    print(f'{k} tem o valor de {v}')
print('-=' * 30)
print(f'O jogador {aproveitamento["nome"]} jogou {len(aproveitamento["gols_marcados"])} partidas')
for i, v in enumerate(aproveitamento['gols_marcados']): #Trabalhando com lista.
    print(f'Na {i+1}ª partida fez {v} gols.')
print(f'Foi um total de {aproveitamento["total_gols"]} gols marcados.')