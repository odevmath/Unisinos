a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

xLinha = ( (b * -1) + (b**2 - 4 * a * c) ** (1/2) ) / (2 * a)
xDuasLinhas = ( (b * -1) - (b**2 - 4 * a * c) ** (1/2) ) / (2 * a)

print("***** Raizes da equação *****")
print("x' =",xLinha)
print("x'' =",xDuasLinhas)