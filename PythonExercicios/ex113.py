#Reescreva a função leiaInt() que fizemos no Desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
#Aproveite e cria também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(msg):
    #loop infinito para que ele fique lendo até que se digite um número certo
    while True:
        #aqui dentro vou passar um try para ele tentar fazer algo
        try:
            n = int(input(msg))
        #se der algum erro vou tratá-lo no except
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor, digite um número inteiro válido.\033[m')
            #uso do continue para jogar no laço novamente
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mERRO! Entrada de dados interrompida pelo usuário.\033[m')
            return 0
        # se não der problema, tudo der certo
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mERRO! Entrada de dados interrompida pelo usuário \033[m')
            return 0
        else:
            return n
        
num = leiaInt('Digite um valor Inteiro: ')
num_2 = leiaFloat('Digite um valor Real: ')
print(f'O valor inteiro digitado foi {num} e o valor real digitado foi {num_2}')
            