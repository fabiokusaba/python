#Desafio 097 Faça um programa que tenha a função chamada escreva(), que recebe um texto qualquer como parâmetro e mostre uma mensagem com tamanhado adaptável.
def escreva(txt):
    print('~' * len(txt))
    print(txt)
    print('~' * len(txt))


#Programa Principal
escreva('Fabio')
escreva('Paralelepipedo')
escreva('Estou assistindo as aulas do Curso em Video')