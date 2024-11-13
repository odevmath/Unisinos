# Exercício 2

userName = input("Por gentileza, informe seu nome: ")

# Usamos uma f-string (indicado pela letra 'f' antes das aspas) para inserir a variável 'userName' diretamente na string.
# Isso facilita a inserção de valores dentro de um texto sem precisar usar concatenação (+).
heightUser = float(input(f"Obrigado, {userName}! Agora, qual é a sua altura? "))

# Novamente, utilizamos a f-string para inserir variáveis dentro da string.
print(f"{heightUser}, entendi. Muito obrigado, {userName}!!")
 