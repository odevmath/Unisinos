pratica = float(input("Informe sua nota na atividade prática: "))
teorica = float(input("Informe sua nota na atividade teórica: "))

provaLab = float(input("Informe sua nota na Prova de Laboratório: "))
testeTeorico = float(input("Informe sua nota no teste teórico: "))
extraclasse = float(input("Informe sua nota no trabalho extraclasse: "))

grauA = (pratica * 0.45) + (teorica * 0.55)
grauB = (provaLab * 0.60) + (testeTeorico * 0.20) + (extraclasse * 0.20)

notaFinal = (grauA * 0.33) + (grauB * 0.67)

mensagem = f'O aluno tirou {
    notaFinal:.2f} na nota final, o que totaliza um aproveitamento de {notaFinal * 10:.2f}%'

print(mensagem)
