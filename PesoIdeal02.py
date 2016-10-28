"""Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que
calcule seu peso ideal, utilizando as seguintes fórmulas:
•Para homens: (72.7 * h) - 58
•Para mulheres: (62.1 * h) - 44.7 (Sabendo que, h = altura)
•Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.
"""

sexo = input("Digite (M) para mulher e (H) para homem: ")

if sexo == "M" or sexo == "m":
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite o peso: "))
    peso_ideal =  (62.1 * altura) - 44.7
    if peso_ideal == peso:
        print("Você está no peso ideal")
    elif peso_ideal > peso:
        print("Você está abaixo do peso ideal")
    else:
        print("Você está acima do peso ideal")

elif sexo == "H" or sexo == "h":
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite o peso: "))
    peso_ideal = (72.7 * altura) - 58
    if peso_ideal == peso:
        print("Você está no peso ideal")
    elif peso_ideal > peso:
        print("Você está abaixo do peso ideal")
    else:
        print("Você está acima do peso ideal")

else:
    print("Digite um valor válido!")

