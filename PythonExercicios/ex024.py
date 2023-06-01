#Desafio 024 Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Digite o nome de uma cidade: ')).title().strip()
print(f'Analisando {cidade}...')
cidade_nome = cidade.upper().split()
santo = cidade_nome[0] in "SANTO"
print(f'Analisando a cidade de {cidade} ela começa ou não com o nome "SANTO"? {santo}.')

#Resolução professor
print(cidade[:5].upper() == 'SANTO')