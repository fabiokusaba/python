#Laços de Repetição (Parte 3)
#Interrompendo repetições while
#Vamos imaginar novamente o nosso personagem só que agora não vamos conseguir saber o tamanho do caminho, mas sabemos que em algum momento tem uma maçã.
#Só que agora temos uma outra coisa que é um troféu, antes tinhamos apenas a maçã e as moedas, agora temos também um troféu que vai ficar localizado numa plataforma superior do nosso caminho.
#O nosso personagem está na busca por maçãs só que se eu encontrar um troféu no meio do caminho eu paro tudo e não preciso mais encontrar maçã se eu tenho um troféu. A idéia então é essa o troféu vai aparecer em uma plataforma superior e se eu encontrar o troféu e pegá-lo eu não preciso mais de maçã e termina o jogo.
#Se eu executasse o código da aula passada em que ele ficaria sendo executado enquanto não encontrar a maçã ele ficaria executando até encontrar a maçã, só que agora tiramos isso então todos aqueles passos ele vai fazer pra sempre, eternamente porque eu não disse nada e retirei aquele enquanto não maçã.
#No momento em que ele encontrar o troféu eu vou fazer uma outra condição: se ele tiver um troféu ele primeiro vai pular, chegou no troféu, ele precisa agora pegar o troféu só que se eu botar um pegar aqui depois que ele pegar o laço vai continuar pra sempre e nunca vai chegar no fim.
#Então ao invés de eu colocar um pegar aqui eu vou colocar um comando novo que é o stop (interromper).
#Esse comando stop vai desviar a execução pro lado de fora do laço, então nesse exemplo do nosso personagem ele viu o troféu ele vai pular vai ser acionado o comando stop que vai desviar o fluxo pra fora, ele vai pegar o troféu e acabou.
#Veja o exemplo no código abaixo:
'''Código abaixo:
enquanto verdadeiro:
    se chao:
        passo
    se buraco:
        pula
    se moeda:
        pega
    se troféu:
        pula
        interrompa
pega
'''
#Para linguagem Python o nosso exemplo ficaria assim:
'''Código abaixo:
while True:
    if chao:
        passo
    if buraco:
        pula
    if moeda:
        pega
    if troféu:
        pula
        break
pega
'''
#Existe um comando no Python para interromper um laço e esse comando é o break.
