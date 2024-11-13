print("DESAFIO MATEMÁTICO")

a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))
c = int(input("Informe o valor de c: "))
d = int(input("Informe o valor de d: "))
e = int(input("Informe o valor de e: "))

areaTriangulo = (b * c) / 2
print (f"\nConsiderando os dados em \"M\" (metros) acerca de um triângulo de base {b} e altura {c}. Temos que sua área é: {areaTriangulo}²")

perimetroRetangulo = a + b + c + d
print (f"\nPara o perímetro de um retângulo, considerando os dados \"M\" (metros), sendo a a fórmula P = 2(b+h), ou a soma de todos os lados, neste caso {a} + {b} + {c} + {d}, temos que o perímetro deste retângulo é: {perimetroRetangulo}")

areaCirculo = 3.14 * (e ** 2)
print (f"\nÁrea de um determinado círculo cujo raio é igual a {e}, considerando \"M\" (metros), é: {areaCirculo}")