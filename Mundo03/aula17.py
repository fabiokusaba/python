#Variáveis Compostas (Listas - Parte 1)
#Tuplas estão entre parêntesis ()
#Listas no Python estão entre colchetes []
#Tuplas e Listas são variáveis compostas, isso quer dizer que elas guardam vários valores.
#Listas são MUTÁVEIS isso quer dizer que elas podem ser mudadas.
#Como as Listas são mutáveis eu posso adicionar elementos novos através do método append(), e veja que esse método append() vai adicionar ao final da minha Lista.
#Em uma Lista eu posso adicionar elementos em outras posições com o método insert() onde primeiro eu vou passar a posição em que eu quero adicionar e em seguida o elemento que eu quero adicionar.
#O comando mais básico para apagar é o del(), uma outra forma de apagar seria utilizando .pop() e normalmente ele é utilizado para apagar o último elemento, mas você também pode utilizar ele para apagar elementos em outras posições passando o seu index.
#E existe ainda um outro método chamado remove() em que eu vou indicar o valor que eu quero eliminar.
#Uma forma de você remover um elemento da Lista em que você não sabe ao certo se ele está ou não é utilizando if in e passando .remove(). Por exemplo:
'''Código abaixo:
if 'Pizza' in lanche:
    lanche.remove('Pizza')
'''
#No exemplo acima nós fizemos que se a pizza estiver no lanche nós vamos removê-la.
#Outra coisa que podemos fazer com as Listas é criar listas através de ranges. Por exemplo:
'''Código abaixo:
valores = list(range(4, 11))
'''
#No código acima nós falamos que o valor é uma lista, perceba que aqui nós utilizamos uma função list() para declarar uma Lista, e partimos de um range de 4 até 11.
#Existe um método para organizarmos as nossas Listas e esse método chama sort() e se quisermos que a nossa ordem seja inversa para passarmos o parâmetro reverse=True dentro do nosso sort().
#Outra coisa que podemos fazer com uma Lista é saber o seu tamanho através do método len()
#O remove() procura do início da Lista a primeira ocorrência do valor que você mandou eliminar e elimina não indo até o final para eliminar outro valor igual, mas conseguimos fazer isso utilizando laços.
#A partir do momento em que eu igualo uma Lista uma com a outra, por exemplo: eu falo que a minha Lista b recebe a minha Lista a, o Python cria uma ligação entre elas e se eu tentar mudar algum elemento de uma das minhas Listas isso se refletirá na outra.
#Mas, existe uma maneira de fazer uma cópia de uma Lista e outra, por exemplo: se eu falo que b recebe a estou fazendo uma ligaçãp (b = a), agora se eu falo que b recebe todos os itens de a[:] e vimos isso quanto estudamos sobre fatiamento, dessa forma estou pegando todos os valores de a e jogando em b então desse jeito ele não vai criar uma ligação, mas sim vai criar uma cópia. E desta forma, se eu mudar algum dos itens de b da seguinte maneira: b[2] = 8 essa mudança só vai ocorrer em b e a permanecerá inalterado. 