#Cria uma função que vai obter o valor, previnir e tratar caso usuário informe alguma coisa que não seja número.
def obterPreco():
  while True:
      try:
        valorProduto = float(input("Por favor, informe o valor do produto: "))
        if valorProduto <= 0:
          print ("Favor: informar um valor válido.")
        else: 
          break #Se o valor for positivo, o loop terminará.
      except ValueError:
        print ("Erro: O valor informado não é um número válido. Insira um valor válido.")
  return valorProduto

#Calcula as taxas de juros e exibe o valor total após aplicação da taxa
def calcularTaxa(valorProduto):
    if valorProduto < 100:
        valorProduto *= 1.10  # Aumento de 10%
    elif valorProduto >= 100 and valorProduto < 300:
        valorProduto *= 1.20  # Aumento de 20%
    elif valorProduto >= 300 and valorProduto < 1000:
        valorProduto *= 1.34  # Aumento de 34%
    elif valorProduto >= 1000:
        valorProduto *= 1.43  # Aumento de 43%
    return valorProduto  # Retorna o valor atualizado

# Função principal para rodar o programa
def main():
   preco = obterPreco()
   precoFinal = calcularTaxa(preco) #Vai jogar o preço obtido e jogar dentro da função para calcular a taxa
   print(f"O valor total a ser pago é de R${precoFinal: .2f}")  # Exibir o valor final

# Chama a função principal
if __name__ == "__main__":
    main()