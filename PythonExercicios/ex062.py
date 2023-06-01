#Desafio 062 Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
#Vou criar uma variável mais_termos para perguntar ao usuário quantos termos a mais ele gostaria de ver.
#Preciso agora colocar toda a minha estrutura dentro de um outro laço é o que chamamos de laços aninhados, ou seja, eu posso aninhar um se dentro de um enquanto, um enquanto dentro de um enquanto, for dentro de um while, posso aninhar qualquer coisa.
#Sabendo disso vou criar um novo while em que vou falar enquanto a minha variável mais_termos que acabei de criar for diferente de 0 ele continua executando e a partir do momento que o usuário digitar 0 ele para e fim do programa.
#Não posso mais condicionar o meu outro while falando que ele vai executar até o contador for menor ou igual a 0 porque agora o meu usuário pode querer digitar outro valor, para solucionar isso eu vou criar uma outra variável total que vai receber o valor 0.
#E vou simular na minha variável mais_termos que o programa vai iniciar com 10 termos porque o usuário vai poder escolher outro valor somente depois.
#Agora eu preciso fazer com que enquanto mais_termos for diferente de 0 o total receba ele mesmo + essa variável mais_termos
#Por fim, podemos mostrar ao usuário quantos termos foram mostrados exibindo a nossa variável total.
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
contador = 1
termo = primeiro_termo
total = 0
mais_termos = 10
while mais_termos != 0:
    total += mais_termos
    while contador <= total:
        print('{} ->'.format(termo), end=' ')
        termo += razao
        contador += 1
    print('PAUSA')
    mais_termos = int(input('Quantos termos você gostaria de mostar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))

