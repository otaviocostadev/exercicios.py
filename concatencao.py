# Faça um programa em Python que receba do usuário duas strings e mostre na tela uma terceira string resultado da
# concatenação (junção) da segunda string com a primeira.

string1 = str(input("Digite a primeira string\n"))
string2 = str(input("Digite a segunda string\n"))
string_resultado = string2+string1
print("A concatenação da segunda string com a primeira é %s" % string_resultado)