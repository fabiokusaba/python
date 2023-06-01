#Desafio 075 Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A)Quantas vezes apareceu o valor 9.
#B)Em que posição foi digitado o primeiro valor 3.
#C)Quais foram os números pares.
#Para eu fazer com que o meu programa leia quatro valores e guarde-os em uma tupla basta eu utilizar os parêntesis, a vírgula e passar 4 vezes o meu input.
#Para eu descobrir quantas vezes o número 9 apareceu na minha tupla eu posso utilizar count().
#Para descobrir em qual posição o número 3 apareceu eu posso utilizar o index() e também posso somar + 1 para a posição ficar mais próximo da nossa realidade visto que tratando-se de índices eles iniciam no 0.
#Para descobrirmos quais foram os números pares vou precisar utilizar do for e dentro do nosso for vamos falar que se o resto da divisão do número por 2 for igual a 0 significa que ele é par então vamos printar esse número.
#Ainda podemos falar que se o valor 3 estiver na minha tupla num vai ser printado na tela a posição em que ele está, caso contrário vai ser printado uma mensagem falando que o valor 3 não foi digitado.
num = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')), int(input('Digite o último número ')))
print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição.')
else:
    print('Nenhum valor 3 foi digitado.')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n}', end=' ')