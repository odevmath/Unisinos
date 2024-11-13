print("Vamos cadastrar seu endereço!")
nomeRua = input("Por gentileza, informe o nome da sua rua: ")
numeroRua = input("Agora o número da sua rua: ")
complementoEndereco = input("Possui complemento? Se sim, informar (ou escreva 'não' se não houver): ")
bairro = input("Informe o seu bairro: ")
cep = input("Informe seu CEP: ")
cidadeEstado = input("Informe sua cidade seguido do Estado (Por exemplo: São Paulo-SP): ")

# Strings formatadas para exibir o endereço
enderecoSemComplemento = f"Endereço: {nomeRua}, {numeroRua}. Bairro: {bairro}, {cidadeEstado} CEP: {cep}"
enderecoComComplemento = f"Endereço: {nomeRua}, {numeroRua}/{complementoEndereco}. Bairro: {bairro}, {cidadeEstado} CEP: {cep}"

# Função para exibir o endereço, considerando o complemento
def start():
    # Se o complemento estiver vazio ou se o usuário digitar "não" ou "Não", imprime o endereço sem complemento
    if complementoEndereco == "" or complementoEndereco.lower() == "não":
        print(enderecoSemComplemento)
    # Caso contrário, imprime o endereço com complemento
    else:
        print(enderecoComComplemento)

# Chamando a função
start()
