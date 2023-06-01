#Laços de Repetição (Parte 1)
#Laços com variável de controle
#Criamos um laço onde o personagem vai caminhar 10 quadradinhos e depois vai pegar a maçã.
'''Código abaixo:
#O c aqui é a nossa variável de controle.
#O range(1, 10) é a quantidade de passos que o nosso personagem vai percorrer
for c in range(1, 10): 
    passo #Um passo por vez
pega #Finalizando ele pega a maçã
'''

#Um outro exemplo: vamos supor agora que ele precise dar um passo e pular três vezes para depois dar outro passo e pegar a maçã.
'''Código abaixo:
#O c aqui é a nossa variável de controle.
#O range(0, 3) é a quantidade de vezes que vai se repetir passo pula.
for c in range(0, 3):
    passo
    pula
passo #Finalizando com passo pega
pega
'''

#Um outro exemplo: mesmo exemplo anterior só que agora acrescentando moedas que nosso personagem pode pegar no meio do caminho.
#Aqui vamos incrementar o pegar moeda com uma estrutura condicional porque ele só vai pegar moeda se existir moeda, caso contrário ele seguirá normalmente.
'''Código abaixo:
#O c aqui é a nossa variável de controle.
#O range(0, 3) é a quantidade de vezes que se repetir passo pula.
#A condição if vai ser executada se tiver uma moeda e tendo uma moeda o personagem vai pegar.
for c in range(0, 3)
    if moeda:
        pega
    passo
    pula
passo
pega
'''
