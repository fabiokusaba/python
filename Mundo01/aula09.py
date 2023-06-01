#Manipulando Cadeias de Texto
#Cadeia de caracteres ou cadeia de texto ou strings e para o Python toda cadeia de caracteres está ou em aspas simples ou em aspas duplas. Por exemplo: 'Curso em Video Python'.
#O Python faz a diferenciação de letras maiúsculas e minúsculas.

#Operações
#Fatiamento: fatiar uma string é conseguir pegar pedaços dela. 
# Por exemplo: frase[9] fatiamento simples em que vou conseguir pegar apenas uma letra, frase[9:13] nesse fatiamento estamos iniciando no 9 até o 13 só que o 13 ele vai excluir então a letra  que está no índice 13 não será incluída, ou seja, vai do 9 ao 13 incluindo o 9 e excluindo o 13, frase [9:21:2] nesse tipo de fatiamento vai iniciar no 9 vai até o 21 e vai pulando de 2 em 2, frase[:5] nesse tipo de fatiamento quando eu não coloco onde ele vai começar ele vai começar do caractere 0 e vai até 5, frase[15:] nesse tipo de fatiamento onde eu indiquei o início mas não indiquei o final e não sabendo o final indica para o Python que eu quero do 15 até o final, frase[9::3] nesse tipo de fatiamente estou indicando que vai começar no 9 e vai até o final já que não estou indicando o outro número e por fim ele vai pular de 3 em 3.
#Análise é saber algumas informações sobre a string como por exemplo: saber o seu tamanho, com que letra ela começa, com que letra ela termina, etc...
#O método len() significa comprimento e vai me dar o comprimento de uma string
#O método count() utilizado para falar para o meu programa contar quantas vezes um caractere aparece. E é possível aqui já passarmos o fatiamento junto, por exemplo count('o', 0, 13).
#O método find() significa encontrar e vai me dizer quantas vezes determinado caractere foi encontrado me passando em qual índice ele se inicia. Quando você passa para o find() uma string que não existe ele vai te retornar -1.
#Eu posso utilizar o operador in para verificar, por exemplo: 'Curso' in frase. Aqui ele vai me retornar um valor boolean, ou seja, True ou False.
#Transformação: via de regra uma lista de string ela é imutável nós não conseguimos mexer nela, mas consigo mudar ela através dos métodos, não consigo mexer direto nos elementos mas eu consigo através de métodos.
#replace() é trocar, reposicionar.
#upper() significa pra cima, ou seja, vai ficar em maiúsculo.
#lower() é o contrário do upper(), ou seja, substitui o que está em maiúsculo para minúsculo.
#capitalize() vai jogar todos os caracteres para minúsculo e só o primeiro caractere ficará em maiúsculo.
#title() vai analisar quantas palavras tem essa string e vai colocar em maiúsculo o primeiro caractere de cada palavra.
#strip() vai remover todos os espaços inúteis no início e no final da string.
#rstrip() vai remover todos os espaços inúteis do lado direito da string, no caso vai remover somente os últimos espaços então se tiver espaços no início ele não vai remover.
#lstrip() vai remover os espaços da esquerda e vai manter os da direita.
#Divisão: posso dividir strings
#split() por padrão ele é feito em seus espaços, vai ter uma divisão dentro da sua string considerando os espaços, cada uma dessas palavras geradas é colocada dentro de uma outra lista então o split ele vai gerar tecnicamente uma lista com todas as palavras da cadeia de caracteres.
#Junção: se eu tenho nomes separados em listas eu consigo juntá-los.
#'-'.join() utilizado para juntar uma coisa na outra, isso significa que você vai juntar todos os elementos e vai usar um separador então ele vai nos mostrar uma string única com essa nova configuração



