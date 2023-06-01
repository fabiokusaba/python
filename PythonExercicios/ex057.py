#Desafio 057 Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
#Uso do strip() para eliminar os espaços vazios
#Uso do upper()[0] aqui combinamos o upper() para deixar a letra em maiúsculo com o fatiamento em que vamos pegar apenas a letra que está no índice [0], ou seja, a primeira letra da palavra.
#Enquanto o sexo não estiver em masculino ou feminino o programa vai continuar perguntando e para isso vamos utilizar o while.
#E podemos escrever nosso flag acima da seguinte forma: while sexo not in 'MmFf'
#Quando o programa terminar eu vou exibir uma mensagem falando que o sexo foi cadastrado com sucesso.
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe o seu sexo: ')).strip().upper()[0]
print('Sexo {} cadastrado com sucesso.'.format(sexo))