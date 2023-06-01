#Desafio 042 Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#Equilátero: todos os lados iguais
#Isósceles: dois lados iguais
#Escaleno: todos os lados diferentes
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um Triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero!')
    elif r1 != r2 != r3 != r1:
        print('Escaleno!')
    else:
        print('Isósceles!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')

#Resolução professor
#Se eu tenho o seguinte exemplo: A == B e B == C posso afirmar automaticamente que A == C porque a igualdade ela é inclusiva, agora a diferença não por exemplo: o A != B, o B != C mas o A == C
#Aqui empregamos a lógica de que se o triângulo não for equilátero, ou seja, ter todos os lados iguais, ou escaleno de ter todos os lados diferentes ele será isósceles assim simplificamos a nossa lógica ao invés de ter que fazer muitas condições para descobrir se um lado é igual ao outro e diferente do outro e assim por diante.
        