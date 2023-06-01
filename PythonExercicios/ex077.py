#Desafio 077 Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar para cada palavra quais são as suas vogais.
#Para cada palavra a gente vai precisar fazer um for.
#Como cada palavra dentro da nossa tupla é considerada uma lista de letras então eu posso fazer o seguinte para cada letra na palavra p posso verificar se a letra estiver no conjunto de vogais 'aeiou'.
palavras = ('Amor', 'Felicidade', 'Perseverança', 'Resiliencia', 'Paciencia', 'Familia', 'Uniao', 'Companheirismo', 'Fidelidade')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
