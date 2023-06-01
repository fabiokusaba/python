#Desafio 083 Crie um programa onde o usuário digita uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
#Vamos primeiro começar lendo a expressão.
#Toda expressão é uma lista também, toda string é uma lista, então eu consigo utilizar um for para pegar cada letra.
#Então vamos criar um pilha que é uma lista vazia.
#Vamos criar um for dizendo o seguinte para cada símbolo de expressão, aqui vamos pegar cada símbolo então eu vou fazer uma verificação para saber se ele é um parênteses abrindo ou fechando.
#Agora eu vou pegar essa minha estrutura de pilha e a cada vez que o parênteses abrir eu vou pegar um parênteses aberto e jogar nessa pilha.
#E a cada vez que eu encontro um parênteses fechando eu tenho duas possibilidades: ou a minha lista está vazia, ou a minha lista está cheia porque pode ser que o meu parênteses fechando esteja no final da lista.
#Então eu vou verificar se o tamanhao da minha pilha for maior que 0 é sinal de que ele não está vazio e ele vai remover o último elemento e para isso vamos utilizar .pop().
#Se não e esse se não é se a pilha estiver vazia daí eu vou dar um .append() na pilha e colocar um caractere de fechamento de parênteses. Isso é sinal de que teve mais parênteses fechando do que abrindo. Vou dar um break para ele parar o laço.
#E aqui fora eu verifico se a minha pilha está cheia ou vazia, ou seja, cada vez que eu abro parênteses eu vou adicionando um parênteses na pilha. Quando eu acho um parênteses fechando eu vou remover um parênteses que eu abri, isso é: cada vez que eu abro eu boto um parênteses abrindo e aí cada vez que eu fecho parênteses eu removo um parênteses abrindo isso é ele já encontrou seu par. Caso a minha pilha esteja vazia eu vou colocar um parênteses fechando e vou dar break, significando que a pilha não está vazia e aí sim dando um erro.
#Verificando fora eu vou fazer que se o comprimento da pilha for igual a 0 é sinal de que cada parênteses que abriu teve sua relação com o parênteses fechando e vou falar que a expressão está válida.
#Se não, isso quer dizer se o comprimento da pilha for acima de 0 vou falar que a expressão está errada.
expr = str(input('Digite a expressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append(símb)
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está inválida.')
