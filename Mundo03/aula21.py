#Funções (Parte 2)
#Interactive Help
#Uma maneira de utilizar a ajuda interativa é através da função interna help()

#docstrings
#Uma docstring basicamente é uma string de documentação, para fazer uma docstring de alguma função sua basta que você abra aspas duplas por 3 vezes logo abaixo de def e coloque as instruções que deseja.

#Argumentos/Parâmetros opcionais
#Vamos pensar em uma funcionalidade que some 3 números: somar(3, 2, 5). Criando essa funcionalidade teríamos def somar(a, b, c) onde o 3 vai para o A, o 2 para o B e o 5 para o C. A soma vai receber: s = a + b + c, e por fim vou escrever o valor: print(f'A soma vale {s}').
#Se eu chamar somar(8, 4) perceba que aqui eu passei menos parâmetros então ele vai pegar o 8 colocar dentro de A, pegar o 4 colocar dentro de B, mas veja que ficou faltando um valor para C e se eu fizer a chamada dessa função dessa maneira isso vai gerar um erro. Mas podemos resolver esse problema utilizando parâmetros opcionais e para isso vou passar que o meu c recebe 0 lá no cabeçalho da minha função então a partir de agora ela ficaria assim: def somar(a, b, c=0).
#E eu posso ter nenhum, um ou todos os meus parâmetros como sendo opcionais.

#Escopo de variáveis
#Na programação basicamente escopo é o local onde uma variável vai existir e o local onde a variável não vai mais existir.
#Eu só uso a variável glogal dentro das funções se eu utilizar a palavra reservada global.

#Retorno de resultados/valores
#Uso da palavra reservada return.
#Funções que retornam resultados são muito úteis quando eu quero ter uma personalização dos resultados, o que eu quero é que ele só me mande os resultados, eu não quero que ele escreva da maneira que ele quiser.
#O return não é apenas para números, você pode retornar um valor lógico verdadeiro ou falso, valores inteiros, valores literais, posso devolver listas, dicionários, tuplas.
