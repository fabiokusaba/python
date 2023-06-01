#Desafio 026 Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A",
#Em que posição ela aparece a primeira vez,
#Em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip()
print('A letra "A" aparece {} vezes na sua frase.'.format(frase.lower().count('a')))
#Adicionamos um para facilitar a leitura da ordem de posição desta forma estamos começando de 1 até o final
print('A posição que a letra "A" aparece a primeira vez é {}.'.format(frase.lower().find('a') + 1))
#Para sabermos qual posição a letra "A" aparece a última vez vamos utilizar rfind() em que ela vai começar do lado direito
print('A posição que a letra "A" aparece a última vez é {}.'.format(frase.lower().rfind('a') + 1))