#Desafio 063 Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
#Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
#Em uma sequência de Fibonacci você vai somar os dois termos anteriores para obter o próximo essa é a lógica por trás.
#Criei minha variável n para ler quantos termos o usuário quer mostrar.
#Os dois primeiros termos da sequência de Fibonacci são definidos automaticamente e correspondem respectivamente a 0 e 1 e pra isso vamos usar as nossas variáveis t1 e t2 para representá-los.
#Eu preciso somar os termos então a minha variável t3 que corresponde ao terceiro termo vai ser a soma do meu t1 e t2.
#Para prosseguir com a sequência eu vou pegar o meu t3 e colocar dentro de um while e a minha variável contador vai iniciar em 3 porque eu já mostrei o primeiro e o segundo termo então eu vou começar a contar do 3.
#E vou passar para o meu while o seguinte: enquanto o meu contador for menor ou igual ao n (que foi lido no início) ele vai ficar repetindo tudo que está dentro dele.
#Passamos o nosso contador recebendo ele + 1.
#Por fim, precisamos fazer a transição de termos, ou seja, eu já tenho os dois primeiros termos: 0 e 1, o meu t3 foi a soma de t1 + t2 que resultou em 1 e foi feito, só que eu preciso agora fazer com que o t1 passe para o lugar que era o t2 e o t2 passe para o lado no lugar que era o t3, assim:
#Uma vez que eu tenha calculado o t3 e mostrado ele na tela eu não preciso mais manter ele então eu faço o meu t1 ser o meu t2 assim como o meu t2 ser o meu t3, assim eles acabam ocupando a posição um do outro. 
#Primeira sequência
#0 - 1 - 1
#t1  t2  t3
#Próxima sequência
#0 - 1 - 1 - 
#    t1  t2  t3

n = int(input('Quantos termos você quer mostar? '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2),end='')
contador = 3
while contador <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    contador += 1
    print('-> {}'.format(t3), end='')
print(' -> FIM!')
