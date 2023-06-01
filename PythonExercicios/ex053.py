#Desafio 053 Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#Ex: Apos a sopa, lendo de trás pra frente o resultado não muda.
#Utilizando strip() para eliminar os espaços antes e depois e upper() para transformá-la em maiúscula.
frase = str(input('Digite uma frase: ')).strip().upper()
frase_separar = frase.split() #Separando a frase pelos espaços, neste caso eu separo numa lista, coleção.
frase_juntar = ''.join(frase_separar) #Juntando a frase e no primeiro argumento eu vou passar a forma que eu quero juntar, neste caso eu juntei desconsiderando os espaços.
frase_inverso = '' #Variável que vai receber a frase invertida.
#Utilizando for para varrer a string de trás para frente.
#Para irmos até a última letra nós podemos pegar len(frase_juntar) - 1
#Para irmos até a primeira letra precisamos passar -1. Lembre-se de que ele sempre precisa ir um a menos e por isso -1.
#E como ele vai voltar, ou seja, passos negativos eu uso -1.
#Para visualizar a frase de trás para frente eu preciso usar frase_juntar[letra].
#Neste problema eu quero que a minha variável frase_inverso seja ele + frase_juntar[letra].

for letra in range(len(frase_juntar) - 1, -1, -1):
    frase_inverso += frase_juntar[letra]
print('O inverso de {} é {}.'.format(frase_juntar, frase_inverso))
#Fazendo a verificação se a frase digitada é ou não um palíndromo.
if frase_inverso == frase_juntar:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

#Uma outra forma de resolvermos o problema sem utilizar o for é utilizarmos o fatiamento de strings, neste caso podemos falar que:
#frase_inverso = frase_juntar[::-1] e neste caso como não estamos passando um início e um fim estamos dizendo para o Python começar do começo e ir até o final, no último parâmetro passamos -1 para representar que queremos de trás para frente.