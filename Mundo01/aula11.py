#Cores no Terminal
#Padrão ANSI padrão de normalização internacional que tem escape sequence que funcionam em vários ambientes.
#Para representar cores no Python você vai fazer da seguinte forma: \033[m e entre o colchetes e o 'm' você vai preencher com cores.
#Podemos passar um código, dois códigos, três códigos ou nenhum código. O primeiro código que vamos passar vai ser o do estilo (style), o segundo código vai ser o do texto (text) e por final o código do background que é a cor de fundo.
#Desta forma, primeiro você vai precisar indicar qual o estilo da fonte (normal, negrito, sublinhada), em segundo lugar você vai informar qual a cor do texto e por último qual a cor do fundo.
#Por exemplo: \033[0;33;44m
#Os códigos para estilo que melhor funcionam no terminal do Python são:
#0 - que significa sem estilo nenhum (None)
#1 - que significa negrito (Bold)
#4 - que significa sublinhado(Underline)
#7 - que significa inversão das configurações o que você colocou para fundo vai para letra, o que você colocou pra letra vai pra fundo (Negative)
#Para a cor do texto:
#30 - branco
#31 - vermelho
#32 - verde
#33 - amarelo
#34 - azul
#35 - roxo (magenta)
#36 - ciano
#37 - cinza
#Para cor de fundo:
#Segue a mesma ordem das cores de texto só que ao invés de 30 aqui começamos com 40 e vamos até o 47.
