#Exemplos

'''a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)'''

#Lembre-se de pular sempre duas entre a sua def e o código principal.
'''def soma(a, b):
    print(f'A soma de A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')'''
    
    
#Programa Principal
#Os valores: 4, 5, 8, 9, 2, 1 são chamados de parâmetros.
#soma(4, 5)
#soma(8, 9)
#soma(2, 1)
# soma(4) #Neste caso a soma vai dar um erro porque a soma recebe dois parâmetros e eu só passei um.
#soma(b=6, a=4) #Posso explicitamente dizer os meus parâmetros e portanto neste caso eu posso mudar a sua ordem.
#soma(7, 2) #Se eu não explicitar a ordem dos parâmetros vai seguir o que foi definido na def, no caso a e b.

#Empacotamento de parâmetros:
#Perceba que aqui os valores foram retornados em tuplas.
#Uso do for para mostrar os valores e formatá-los.
'''def contador(* núm):
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM!')
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números.')
    
    
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

#Dobrando os valores da minha lista
'''def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)'''

#Empacotamento e desempacotamento:
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos a soma {s}')


soma(5, 7)
soma(2, 9, 4)
