#Desafio 089 Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
#Primeiro vamos declarar uma ficha padrão para cada aluno.
#Vamos criar uma variável simples que vai ler o nome e as notas do aluno. E uma variável média para armazenar o cálculo da média das notas.
#Agora vamos dar um .append() nessas variáveis.
#Já que eu quero que isso aconteça várias vezes vamos criar um loop infinito com while True
#Vou criar uma resposta para perguntar se ele deseja continuar ou não.
#Agora vou utilizar um for para mostrar os dados.
#Agora eu vou mostrar as notas do aluno e para isso vou criar um outro loop infinito com while True.
#Agora se opc for menor ou igual ao len(ficha) - 1, isso é se eu digitar que cadastrei o aluno 0, 1 e 2, ele tem que ser 0, 1 ou 2, não podendo ser 3, 4, 5, por isso ele tem que ser menor que len(ficha) que é a quantidade de alunos que tenho cadastrado - 1 porque o primeiro aluno é 0 e o último é n-1.
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome,[nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
#Fazendo um for para mostrar os dados
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? [999 para parar]: '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('VOLTE SEMPRE!')