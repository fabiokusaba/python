def leiaDinheiro(msg):
    valido = False #flag iniciando com falso porque ele não é válido ainda.
    while not valido:
        #apesar de ser uma entrada eu vou colocar em string para eu poder ler ele e depois tratá-lo
        #vou utilizar replace para substituir todas as vírgulas por pontos
        entrada = str(input(msg)).replace(',', '.').strip()
        #se a entrada for alfanumérico vou exibir uma msg 'Preço inválido'
        #ou se a entrada tirando os espaços for igual a vazio
        if entrada.isalpha() or entrada == '': 
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m') #alterando a cor para vermelho
        else: #se ele não for alfa:
            valido = True #minha flag passa a ser True
            return float(entrada) #vou retornar minha entrada convertida para float
    