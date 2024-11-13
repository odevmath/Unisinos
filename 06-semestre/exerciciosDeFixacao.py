#Exercício 1:
'''
valor = int(input("Informe um valor: "))

if valor % 2 == 0:
  print("O valor informado é par!")
else:
  print("O valor informado é ímpar!") '''

# Exercício 2:

'''
a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))

if b < 0:
  print("Erro: o valor de B não deve ser menor ou igual a 0")

divisao = int(a / b)

print(f"A divisão de A por B é igual a: {divisao}")
'''

# Exercício 3:
'''
ano = int(input("Informe o ano: "))

if ano % 4 == 0:
  print(f"{ano} é um ano bissexto!")
else:
  print(f"{ano} não é um ano bissexto.")
'''

# Exercício 4:
'''
grauA = float(input("Informe a nota recebida em Grau A: "))
grauB = float(input("Informe a nota recebida em Grau B: "))

if grauA < 0 or grauB < 0:
  print("Uma das notas informadas não é válida!")
  exit()
elif grauA >= 0 and grauB >= 0: 
  media = (grauA * 0.3) + (grauB * 0.7)
  if media >= 6.0 :
    print(f"Aluno aprovado com média de {media: .2f} e não precisa realizar a avaliação Grau C.")
  else:
    print (f"Aluno ainda não está aprovado, será necessário realizar a avaliação Grau C. Sua média foi de {media}")
    exit()
'''

# Exercício 5:
'''
vogais = ['a', 'e', 'i', 'o', 'u']
letra = input("Informe uma letra: ").lower()

if letra in vogais:
  print("A letra informada é uma vogal.")
else: 
  print("A letra informada é uma consoante.")
'''

# Exercício 8:
'''
variavel = 0
print(variavel)

while variavel < 1000:
  variavel = variavel + 1
  print(variavel)
'''

# Exercício 9:
'''
valor = 0
while valor < 2002:
  print(valor)
  valor = valor + 2
'''
# Exercício 10:
'''
valor = 1000
print(valor)
while valor > 0:
  valor = valor - 1
  print(valor)
'''

# Exercício 11:
'''
cont = 0
soma = 0
while cont < 10:
  valor = int(input("informe um valor: "))
  soma += valor
  cont += 1
print("A soma dos valores é: ", soma)
'''

# Exercício 13:
'''
for i in range(1,101):
  print(i)
'''

# Exercício 14:
'''
valor = int(input("Informe um valor de 1 à 10: "))
tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in tabuada:
  resultado = valor * numero
  print(f"{valor} x {numero} = {resultado}")
'''

#Exercício 15

quantidade = int(input("Informe a quantidade de itens que serão inseridos à lista: "))
lista = []

for i in range(quantidade):
  produto = input(f"informe o produto {i + 1}: ")
  lista.append(produto)

print ("\nSua lista de compras: ")

for produto in lista:
  print(f"- {produto}")
