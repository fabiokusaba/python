#Desafio 073 Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol na ordem de colocação. Depois mostre:
#A)Apenas os 5 primeiros colocados.
#B)Os últimos 4 colocados da tabela.
#C)Uma lista com os times em ordem alfabética.
#D)Em que posição na tabela está o time da Chapecoense.
#OBS: Utilizei o +1 no index porque quando estamos trabalhando com índices eles iniciam no 0 e vão até o final e no caso como estamos trabalhando com uma tabela de um campeonato não existe a posição 0, mas sim o primeiro lugar, por isso adicionamos 1.
times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos',
         'Ceará SC', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')
print(f'Os 5 primeiros colodados são: {times[0:5]}')
print(f'Os últimso 4 colocados da tabela são: {times[-4:]}')
print(f'{sorted(times)}')
print(f'A Chapecoense está na {times.index("Chapecoense") + 1}ª posição.')