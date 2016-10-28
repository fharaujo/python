"""Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que
calcule seu peso ideal, utilizando as seguintes fórmulas:
•Para homens: (72.7 * h) - 58
•Para mulheres: (62.1 * h) - 44.7 (Sabendo que, h = altura)
•Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.
"""

homem_altura = 1.80
mulher_altura = 1.60

peso = float(input("Digite o peso: "))

peso_ideal_homem = (peso * homem_altura) - 58
peso_ideal_mulher =  (peso * mulher_altura) - 44.7

print("Homem com peso ideal: ", peso_ideal_homem)
print("Mulher com peso ideal ", peso_ideal_mulher)
