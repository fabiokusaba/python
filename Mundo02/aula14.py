#Laços de Repetição (Parte 2)
#Estrutura de repetição com teste lógico vai ter uma condição que enquanto não for satisfeita o laço irá continuar, uma vez satisfeita ela sai do laço e segue o seu fluxo normal.
#Vejamos o seguinte exemplo: nosso personagem precisa pegar uma mação mas não sabemos quantos passos ele precisa dar para chegar até ela então nesse caso vamos utilizar while que significa 'enquanto' e podemos traduzir o nosso código da seguinte forma: enquanto nosso personagem não chegar na maçã dê passo, chegando na maçã ele vai parar de dar passo, vai sair daquele loop de passo que ele estava, vai pegar e maçã e finalizou o nosso programa.
'''Código abaixo:
while not mação:
    passo
pega
'''
#Vamos pensar num outro exemplo para o nosso personagem: não sabemos quantos passos serão necessários para chegar até a maçã mas também no meio do caminho temos buracos, moedas que podemos pegar, ou seja, criou-se alguns desvios em nossa trajetória.
#Para solucionarmos esses desvios no nosso trajeto vamos continuar utilizando o enquanto só que agora vamos utilizar também as condições que vimos em aulas anteriores, então podemos criar a seguinte condição: se tiver chão dê um passo, se tiver um buraco pule, se tiver uma moeda pegue, e perceba que aqui o nosso personagem vai ficar repetindo a verificação dessas condições toda vez até chegar na maçã. Chegando na maçã a condição que colocamos no início 'while not maçã' vai ser falsa então ele vai sair do laço pegar e maçã e finalizar o nosso programa.
#Vamos verificar como isso ficaria no código.
'''Código abaixo:
while not maçã:
    if chão:
        passo
    if buraco:
        pula
    if moeda:
        pega
pega
'''
#Quando eu sei o limite posso usar o for e posso usar o while ficando ao meu critério, mas quando eu não sei o limite eu preciso utilizar o while.
#Com o while com a estrutura enquanto eu posso criar situações onde eu faça laços indeterminadamente. Eu não tenho que determinar um range.