#
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #Utilização de [:] para fazer uma cópia
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) #Utilização de [:] para fazer uma cópia
print(galera)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[2][0])
#print(p) - vai fazer uma lista
#p[0] - para nomes
#p[1] - para idade
for p in galera:
    print(p)
    
#Outra coisa que posso fazer é pedir nome e idade e para isso vou criar a minha variável galera que vai ser uma lista e aí eu vou criar uma estrutura que chama dado que vai pegar temporariamente os dados dessa lista.
#Por exemplo: vou pegar o dado de 5 pessoas e jogar na minha lista galera. Lembrando que tem que ser a cópia do dado. Logo em seguida vou pegar o dado e excluir utilizando .clear().
#Vamos supor agora que eu queira mostrar somente as pessoas maiores de 21 anos e pra isso eu posso criar um for.
#Para idade vamos passar [1] já que [0] simboliza nosso nome e [1] simboliza nossa idade.
#Posso ainda criar uma variável totalmaior e totalmenor para saber a quantidade de maiores e menores de idade.
galera = list() #Estrutura de dados principal.
dado = list() #Estrutura de dados auxiliar onde eu vou pegar os dados para depois ir na estrutura principal.
totalmaior = totalmenor = 0 #Verificar o total de maiores e menores de idade.
for c in range (0, 5): #Toda essa estrutura é para eu ler os dados e jogar dentro da galera.
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #Faz uma cópia de dados em galera.
    dado.clear() #Apaga os dados a cada vez que eu faço o laço.
for p in galera: #Analisando para ver se a pessoa (p) é maior ou menor.
    if p[1] >= 21:
        print(f'{p[0]} é maior de 21 anos.')
        totalmaior += 1 #Totalizando para mostrar o maior de idade.
    else:
        print(f'{p[0]} é menor de idade.')
        totalmenor += 1 #Totalizando para mostrar o menor de idade.
print(f'Temos {totalmaior} maiores e {totalmenor} menores de idade.')