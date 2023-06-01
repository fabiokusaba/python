#No Python novo eu posso criar uma tupla com ou sem parêntesis.
#Na hora de referenciar os elementos da minha tupla eu sempre vou utilizar colchetes.
#Lembre-se que na hora em que eu vou fazer o fatiamento o último elemento é ignorado, então por exemplo: se eu for fazer o fatiamento de [1:3] o elemento que ocupa o índice 3 que é o Pudim vai ser ignorado só mostrando Suco e Pizza.
#Tuplas são imutáveis isso significa que eu não consigo atribuir valores a tupla a não ser na sua declaração.
#vejamos um exemplo com for.
#Uma outra forma de utilizar o for é combinando com o método len(). Vejamos.
#Quando você precisar mostrar posição é preferível usar o for cont in range(0, len()) passando a nossa tupla, ou você pode utilizar também o for pos, comida in enumerate(lanche) onde ele vai me dar a comida e também a sua posição.
#Existe um método chamado sorted() que quer dizer organizado, em ordem.

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#Se eu não precisar de posição posso utilizar a forma clássica:
for comida in lanche:
    print(f'Eu vou comer {comida}.')

#Se eu precisar mostrar a posição, tenho as seguintes formas:
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}.')
    
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')

print('Comi pra caramba!')

#Outra coisa que podemos fazer com tuplas, vamos criar duas tuplas a e b contendo números.
#Imagine que eu faça uma tupla c que seja a + b, quando eu uso + em tupla ele vai juntar as tuplas para formar a nova.
#Aqui perceba que a tupla c não vai ser a mesma coisa que b + a porque a ordem aqui tem total influência.
#A tupla tem alguns métodos internos e um deles é o count() que quer dizer quantas vezes algo está aparecendo na tupla.
#Além do count() eu ainda tenho a propriedade index() da tupla em que vai nos motrar a posição do elemento.
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b

#No Python não tenho essa limitação de só colocar números ou só colocar letras, aqui eu posso misturar os dois, ou seja, eu posso ter dados de tipos diferentes nas minhas tuplas. Veja:
pessoa = ('Fabio', 27, 'M', 61)
print(pessoa)

#Como dissemos a tupla é imutável, ou seja, a gente não pode nem eliminar um elemento, nem adicionar um, nem modificar um elemento que já está dentro da tupla. Só que eu posso fazer uma coisa dentro da tupla que é apagar ela toda utilizando del().
del(pessoa)