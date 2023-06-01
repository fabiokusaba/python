#Desafio 095 Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
time = list()
jogador = dict()
partidas = list()
#Leitura de dados
while True:
    jogador.clear() #Apagando os dados do jogador antes de ler ele para poder limpar porque a cada laço eu vou ler dados de um jogador.
    jogador['nome'] = str(input('Nome do Jogador: ')) #Lendo o nome do jogador.
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? ')) #Total de partidas.
    partidas.clear() #Apagando os dados da partida antes de ler.
    for p in range(1, tot + 1): #Uso do for para perguntar os gols marcados em cada partida.
        partidas.append(int(input(f'Quantos gols na {p}º partida? ')))
    jogador['gols'] = partidas[:] #Fatiamento da minha lista partidas para dentro do meu dicionário jogador, no caso estou fazendo uma cópia.
    jogador['total'] = sum(partidas) #Soma dos gols.
    time.append(jogador.copy()) #Jogando os dados do meu dicionário jogador na minha lista time.
    while True: #Validação se o usuário deseja continuar ou não.
        resp = str(input('Deseja cadastrar outro jogador? [S/N]: ')).strip().upper()[0]
        if resp in 'SsNn':
            break
        print('ERROR! Por favor, digite apenas [S/N]')
    if resp in 'Nn':
        break
print('-=' * 30)
#Exibindo os resultados.
print('cod ', end='')
for c in jogador.keys(): #Para cada chave em jogador.keys()
    print(f'{c:<15}', end='') # Cabeçalho para mostrar o nome das chaves.
print() #Quebra de linha
print('-' * 40)
for i, v in enumerate(time): #Uso do for in enumerate() já que o time é uma lista.
    print(f'{i:>3} ', end='')
    for d in v.values(): #Para cada dado em valor.values(), aqui estamos trabalhando com dicionário.
        print(f'{str(d):<15}', end='')
    print() #Para quebra de linha já que eu mostrei todas as colunas.
print('-' * 40)
#Exibindo os dados de um jogador escolhido pelo usuário.
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999: #flag se a busca for igual a 999 o programa para.
        break
    if busca >= len(time): #Verificando se a busca for maior ou igual ao tamanho do time vai ser exibido uma mensagem de erro.
        print(f'ERROR! Não existe jogador com o código {busca}.')
    else: #Se não, estando dentro do limite ele vai exibir o jogador.
        print(f'Levantamento do Jogador {time[busca]["nome"]}: ')
        #Para mostrar o levantamento do jogador vou precisar de um for enumerate já que estou trabalhando com uma lista, dessa lista vou passar a busca e vou querer a chave ['gols']
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('LEVANTAMENTO ENCERRADO!')