#Erros e Exceções
#Dentro de try vamos colocar o que geralmente pode dar problema, qual é o comando ou quais são os comandos que normalmente dariam problemas.
#E no except você vai colocar a área da falha que é se eu tentar no try e falhar o que que vai acontecer.
#Se por acaso não der problema aí eu vou usar o else e dentro da área else eu vou dizer o que vai acontecer se deu certo, se meu try deu certo.
#Temos uma outra cláusula que podemos colocar logo abaixo do else e essa última cláusula é o finally quer dizer finalmente e ele vai acontecer independente se deu certo ou se deu erro.
#As cláusulas else e finally são opcionais nem sempre você vai precisar utilizar.
#No meu except eu posso fazer exibir o erro utilizando Exception as e o nome de uma variável que eu quiser para exibir esse meu erro, por exemplo: Exception as erro.
#Essa estrutura pode se expandir muito, na verdade todo try pode ter mais de um exception em que um ganhará um TypeError e eu posso ter vários excepts para outros tipos de exceção e cada um deles vai ter o seu próprio bloco, com sua própria mensagem, com seu próprio tratamento.
#Resumindo um mesmo try pode ter vários excepts.