# Faça um programa em Python que receba do usuário uma medida em metros e exiba na tela ela convertida para centímetros.

metros = float(input("Digite a medida em metros\n"))
centimetros = metros * 100
print("%.2f metros correspondem à %.2f centímetros" % (metros, centimetros))