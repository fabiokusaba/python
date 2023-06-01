#Desafio 080 Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
#No final, mostre a lista ordenada na tela.
#Eu preciso ler um número só que eu não posso ler e já ir colocando no .append() porque senão esse número vai ser sempre colocado no final. Então eu vou ter uma variável n que vai ler os números.
#Agora eu preciso descobrir em qual posição eu vou ter que adicionar e pra isso eu tenho três possibilidades: ou ele é o primeiro valor, ou então ele é o último valor da lista, ou então ele vai estar no meio.
#Então vou verificar se é o primeiro valor basta eu incluir ele na lista, aqui eu não vou precisar ficar verificando posição.
#Agora eu vou verificar se o número é maior do que o número que está no último elemento da minha lista. E para eu pegar o meu último elemento basta eu fazer lista[len(lista)-1] ou simplesmente lista[-1]. E aqui eu também vou fazer um lista.append(n).
#E podemos simplificar a nossa lógica falando que se o c for igual a 0 ou n for maior que o meu último elemento eu vou dar lista.append(n).
#Agora precisamos verificar em que posição eu vou adicionar se o meu valor ficar no meio e para eu fazer essa verificação eu vou varrer a lista inteira.
#Pra isso vou criar uma variável pos (posição) que começa com 0 e utilizando um while vou dizer que enquanto pos for menor ao comprimento da minha lista, ou seja, ele vai da posição 0 até a última posição. Então eu vou verificar se o número que eu quero inserir que é o n é menor ou igual a lista na posição pos.
#Aqui eu estou verificando em cada posição se o número que eu quero inserir é menor ou igual a ele, e se ele for menor ou igual eu vou inserir esse valor numa posição específica e para isso eu não vou usar o .append(), vou utilizar o insert(). Então eu vou falar que vou inserir na lista na posição pos o n, e como eu não vou precisar mais eu posso dar um break. E não podemos esquecer de dar pos += 1 para poder ficar passando na posição
lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[len(lista)-1]:
        lista.append(n)
        print('Adiciona ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
               lista.insert(pos, n)
               print(f'Adicionado na posição {pos} da lista')
               break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')