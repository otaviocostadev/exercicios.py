# Faça um programa em Python que peça as 4 notas e mostre a média com 2 casas decimais.

n1 = float(input("Digite a primeira nota\n"))
n2 = float(input("Digite a segunda nota\n"))
n3 = float(input("Digite a terceira nota\n"))
n4 = float(input("Digite a quarta nota\n"))
media = (n1+n2+n3+n4) / 4
print("A média das quatro notas é %.2f" % media)