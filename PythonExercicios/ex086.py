#Desafio 086 Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.
#Como eu já sei a quantidade de elementos eu vou criar uma variável matriz que vai ser a minha lista e dentro dela eu vou ter outras 3 listas dentro que vão representar as minhas linhas.
#Dentro de cada linha eu vou ter três valores dentro então eu vou representar por 0 pra ele ficar vazio e eu não precisar usar .append().
#E agora o que eu preciso fazer é substituir os zeros por valores.
#Agora eu preciso fazer um laço dentro do outro para eu poder suprir todas as linhas e colunas.
#Começando com a linha vou fazer um for com range de (0, 3), e dentro desse meu for de linha eu vou fazer um for de colunas com range de (0, 3).
#Agora eu vou jogar dentro da matriz que ela vai receber um valor inteiro de um input, só que eu preciso colocar em matriz na linha l e na coluna c.
#Vamos fazer novamente um for com a linha dentro da coluna para organizar a nossa matriz 3x3
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#for de alimentação onde eu vou colocar os valores dentro da matriz.
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
#Mostrar a estrutura na tela 3x3
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
