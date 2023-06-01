#Desafio 061 Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
#Vamos precisar de uma variável para o termo e uma variável contador, a nossa variável termo vai receber o nosso primeiro_termo e o nosso contador vai começar com 1 porque eu quero que ele me mostre os 10 primeiros termos.
#Resumindo a nossa variável termo vai mostrar o termo em si e a nosas variável contador vai contar quantos termos foram.
#E a lógica que vamos utilizar vai ser a seguinte: enquanto o contador for menor ou igual a 10 ele vai mostrar o termo e vai receber contador += 1.
#Antes da gente somar o contador += 1 vamos passar o nosso termo += razao
print('Gerador de PA')
print('=-=' * 10)
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro_termo
contador = 1
while contador <= 10:
    print('{} ->'.format(termo), end=' ')
    termo += razao
    contador += 1
print('FIM!')
