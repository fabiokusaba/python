#Desafio 048 Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
contador = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        soma += c
        contador += 1
print('A soma de todos os {} números é {}.'.format(contador, soma))

#Resolução do professor
#Para mostrar apenas os números ímpares podemos colocar o nosso range(1, 501, 2), ou seja, iniciando em 1 indo até 500 e pulando de 2 em 2 desta forma vamos pegar somente os números ímpares fazendo menos esforço.
#Para mostrarmos apenas os números múltiplos de 3 podemos fazer da seguinte forma: c % 3 == 0, ou seja, o resto da divisão com 3 tem que ser igual a 0 para ser considerado múltiplo de 3.
#Para fazermos agora a soma precisamos usar o conceito de acumulador sendo assim vamos criar uma variável soma para indicar o nosso acumulador e essa variável vai receber 0, ou seja, por enquanto eu não tenho nenhum número divisível por 3 e ímpar.
#E para realizarmos essa soma fazemos da seguinte maneira: soma = soma + c ou de forma simplificada soma += c.
#Além do acumulador nós vamos adicionar um contador para sabermos quantos números foram somados, desta forma vamos criar uma variável contador para representar o nosso contador e essa variável vai receber 0 e aqui para cada vez que ocorrer o laço eu vou fazer: contador = contador + 1 ou de forma simplificada contador += 1
