#Se eu uso a estrutura while True ele vai executar tudo o que estiver dentro do seu bloco para sempre e a única coisa que vai fazer esse enquanto parar é eu apertar o stop ou o comando break, então o comando break quebra um loop que está acontecendo numa determinada sequência de vezes.
#Vamos para alguns exemplos: vamos supor que eu queira ler um número inteiro e que eu queira fazer a soma dos números que eu digitei excluindo-se o número 999 que vai ser considerado o flag do meu loop, ou seja, o ponto de parada.
#Para realizarmos essa soma podemos fazer da seguinte maneira: inicializamos nossa variável soma (s) ali fora e atribuimos a ela o valor de 0.
#Criamos uma condição if que se o número (n) for igual a 999 o comando break vai ser lido e irá ocorrer um desvio no nosso programa e dessa forma ele não será utilizado para o cálculo da nossa soma.
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma dos valores é {}.'.format(s))