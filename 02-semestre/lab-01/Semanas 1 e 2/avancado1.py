"""
Potencia: NUM1 ** NUM2 
Radiciação: NUM1 ** (1/NUM2)  ==> Parênteses dão precedência!
-> 25 ** (1/2) -> raiz quadrada de 5
-> 27 ** (1/3) -> Raiz cúbica de 9
"""

"""Faça um programa em Python que:
=> Receba um float digitado pelo usuário e armazene em A
=> Receba um float digitado pelo usuário e armazene em B
==> Imprima as seguintes mensagens na tela (substitua o X e o Y) pelo resultado da operação indicada na mensagem):
- "A multiplicado por B é X"
- "A dividido por B é X"
- "A mais B é X e A menos B é Y"
- "A elevado a B é X"
"""

a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))
c = int(input("Informe o valor de C: "))
d = int(input("Informe o valor de D: "))

"""
print(f'{a} multiplicado por {b} é:', a*b)
print(f'{a} dividido por {b} é:', a/b)
print(f'{a} somado a {b} é:', a+b)
print(f'{a} elevado a {b} é:', a ** b)
"""

xLinha = ((b * -1) + (b**2 - 4 * a * c) ) ** (1/2) / (2 * a)
xDuasLinhas = ((b * -1) - (b**2 - 4 * a * c) ) ** (1/2) / (2 * a)

print("***** Raízes da Equação *****")
print("x' =", xLinha)
print("x'' =", xDuasLinhas)