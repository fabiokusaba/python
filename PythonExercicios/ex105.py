#Desafio 105 Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#Quantidade de notas
#A maior nota
#A menor nota
#A média da turma
#A situação (opcional)
#Adicione também as docstrings da função.
#A minha variável r vai ser um dicionário e nele eu vou ter vários campos: total que vai ser a quantidade de notas, maior que vai receber a maior nota, também vou ter o menor que vai receber a menor nota, vou ter também a minha média que vai ser a sum(n) dividido pela len(n).
#Vou também adicionar a situação e se a situação for verdadeira: 
def notas(* n, situação=False):
    """_summary_
    -> Função para analisar notas e situações de vários alunos.
    n: aceita uma ou mais notas dos alunos
    situação: (opcional) indicando se deve ou não adicionar a situação.
    Returns:
        return: dicionário contendo várias informações da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if situação:
        if r['média'] >= 7:
            r['situção'] = 'BOA'
        elif r['média'] >= 5:
            r['situção'] = 'RAZOÁVEL'
        else:
            r['situção'] = 'RUIM'
    
    return r
     

#Programa Principal
resp = notas(5.5, 2.5, 1.5, situação=True)
print(resp)
#help(notas)