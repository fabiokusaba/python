'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for chave, valor in pessoas.items():
    print(f'{chave} = {valor}') '''
    
'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['sigla'])'''

estado = dict()
brasil = list()
#Lendo três estados com for.
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')) #Lendo pelo teclado UF.
    estado['sigla'] = str(input('Sigla do Estado: ')) #Lendo pelo teclado a sigla.
    brasil.append(estado.copy()) #Adicionando o meu dicionário estado na minha lista brasil. Existe um método interno no dicionário para que eu possa copiar o conteúdo e esse método é chamado de copy().
#Utilizando for
#Para cada Estado em Brasil eu mostro o Estado.
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()