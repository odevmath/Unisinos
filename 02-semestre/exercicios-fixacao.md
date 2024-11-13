# ⇒ Exercícios de fixação

## Exercício 1

Crie um programa que recebe um inteiro pelo teclado e imprime se ele é par ou ímpar.

```python
valor = int(input("Informe um valor: ")) #Recebe o valor

if valor % 2 == 0: #Faz a divisão por 2 e verifica se o resto é 0
  print("O valor informado é par!") #Se o resto da divisão for 0
else:
  print("O valor informado é ímpar!") # Se o resto da divisão for > 0
```

## Exercício 2

Crie um programa que recebe dois valores inteiros A e B pelo teclado e imprime o valor de A dividido por B. Entretanto, se o valo de B for 0, imprima uma mensagem de erro e não faça a divisão.

```python
a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))

if b < 0:
  print("Erro: o valor de B não deve ser menor ou igual a 0")

divisao = int(a / b)

print(f"A divisão de A por B é igual a: {divisao}")
```

## Exercício 3

Crie um programa que recebe um valor inteiro referente a um determinado ano. Imprima na tela se o ano informado é bissexto ou não (para simplificar, você pode utilizar apenas a informação de o ano é divisível por 4 ou não).

```python
ano = int(input("Informe o ano: "))

if ano % 4 == 0:
  print(f"{ano} é um ano bissexto!")
else:
  print(f"{ano} não é um ano bissexto.")
```

## Exercício 4

Crie um programa que recebe a nota do Grau A e a nota do Grau B pelo teclado e imprime na tela se será necessário ou não realizar o Grau C (considere o sistema de avaliação da Unisinos, sendo o GA valendo 30% e o GB valendo 70%). Caso algum valor informado seja negativo, informe uma mensagem de erro e não realize o cálculo.
```python
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
```

## Exercício 5

Crie um programa que solicita que o usuário digite uma letra e imprime na tela se a letra é uma vogal ou uma consoante.
```python
vogais = ['a', 'e', 'i', 'o', 'u']
letra = input("Informe uma letra: ").lower()

if letra in vogais:
  print("A letra informada é uma vogal.")
else: 
  print("A letra informada é uma consoante.")
```


## Exercício 6
**Pergunta:** O que é um parâmetro de entrada de um método?

**Resposta:** Um **parâmetro de entrada** de um méto é uma variável definida na assinatura do método, fazendo com que o método receba dados quando é chamado, por exemplo: 
```python
def saudacao(nome):  # 'nome' é o parâmetro de entrada
    print(f"Olá, {nome}!")
saudacao("Fulano")  # "Fulano" é o argumento passado para o parâmetro 'nome'
```
### Diferença entre parâmetros e argumentos:**
**Parâmetros:** São as variáveis definidas no cabeçalho do método para receber os dados de entrada (ex: nome). <br>
**Argumentos:** São os valores efetivamente passados para os parâmetros quando o método é chamado (ex: "Fulano").

## Exercício 7

**Pergunta:** O que é o retorno de um método? <br>
**Resposta:** O retorno de um método é o valor que o método/função retorna após esecutar as instruções recebidas. Este retorno pode ser usado para a continuação do programa ou armazenado em uma variável. <code>return</code> é a sintaxe utilizada para retorno.

## Exercício 8

Utilizando while, crie um programa que imprime os números de 0 a 1000.

```python
variavel = 0
print(variavel)

while variavel < 1000:
  variavel = variavel + 1
  print(variavel)
```
## Exercício 9

Utilizando while, crie um programa que imprime os números pares de 0 a 2000.

```py
valor = 0
while valor < 2002:
  print(valor)
  valor = valor + 2
```

## Exercício 10

Utilizando while, crie um programa que imprime os números de 0 a 1000 em ordem decrescente (ou seja, de 1000 a 0).

valor = 1000
print(valor)
while valor > 0:
  valor = valor - 1
  print(valor)

## Exercício 11

Utilizando while, crie um programa que solicita para o usuário que ele digite 10 valores inteiros. Ao final, imprima a soma de todos os valores digitados.

## Exercício 12

Comparando os comandos de repetição for e while, em quais ocasiões é mais comum a utilização de um ou de outro?

**While:** geralmente é mais utilizado quando não sabemos a quantidade de repetições que nosso código fará. Por exemplo, “enquanto o usuário não acertar o usuário e a senha, peça novamente”. <br>
**For** é mais utilizado quando sabemos o número de iterações a realizar. Por exemplo, “o usuário possui 5 tentativas para acertar o usuário e a senha”.

## Exercício 13

Utilizando for, crie um programa imprime na tela os valores de 1 a 100 (incluindo o 1 e o 100).
```py
for i in range(1,101):
  print(i)
```

## Exercício 14

Utilizando for,crie um programa que imprime a tabuada de um número inteiro digitado pelo usuário.

```py
valor = int(input("Informe um valor de 1 à 10: "))
tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in tabuada:
  resultado = valor * numero
  print(f"{valor} x {numero} = {resultado}")
```


## Exercício 15

Crie um programa que permita que o usuário crie sua lista de compras. Primeiramente, solicite que ele informe quantos produtos serão adicionados na lista. Depois disto, peça para que o usuário digite os produtos que ele vai comprar, e armazene em uma lista. Ao final, imprima a lista de compras do usuário.

```py
quantidade = int(input("Informe a quantidade de itens que serão inseridos à lista: "))
lista = []

for i in range(quantidade):
  produto = input(f"informe o produto {i + 1}: ")
  lista.append(produto)

print ("\nSua lista de compras: ")

for produto in lista:
  print(f"- {produto}")
```
