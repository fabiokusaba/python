#Desafio 004 Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
algo = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(algo)}')
print(f'É um número? {algo.isnumeric()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'Está em maiúsculo? {algo.isupper()}')
print(f'Está em minúsculo? {algo.islower()}')
print(f'Só tem espaços? {algo.isspace()}')
print(f'Está capitalizada? {algo.istitle()}')

#O algo nesse código é um objeto e todo objeto tem características e realiza funcionalidades então eles tem atributos e métodos, no caso tudo que está após o nosso algo e contém parêntesis nós chamamos de métodos
#Todo objeto string tem esses métodos isnumeric(), islower(), isupper(), etc...