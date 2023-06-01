#try except else
try: #vai tentar executar o código que estiver aqui.
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
#except Exception as erro: #se der falha no meu try vai executar o código que estiver aqui.
#    print(f'Problema encontrado foi {erro.__class__}') #utilizando Exception para exibir o meu erro, no caso a sua classe.
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi: {erro.__cause__}')
else: #se der êxito no meu try vai executar o código que estiver aqui.
    print(f'O resultado é {r:.1f}')
finally: #o código que estiver aqui vai acontecer independente se der certo ou se deu erro.
    print('Volte sempre! Muito obrigado!')