trabalho = float(input("Informe a nota que você tirou no trabalho: "))
prova = float(input("Informe a nota que você tirou na Prova: "))
teste = float(input("Informe a nota que você tirou no teste: "))

notaFinal = (trabalho * 0.1) + (teste * 0.60) + (prova * 0.30)
media = trabalho + teste + prova
mensagem = f'O aluno pontuou uma nota final de {
    notaFinal}, que corresponde a {notaFinal * 10:.2f}% de aproveitamento!'
print(mensagem)
