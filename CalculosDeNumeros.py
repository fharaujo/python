"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
* o produto do dobro do primeiro com metade do segundo.
* a soma do triplo do primeiro com o terceiro.
* o terceiro elevado ao cubo."""
#autor: @fharaujo
#data: 28/10/2016
#Projeto: APrendendo Python - Estrutura Sequencial

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

produto = (numero1 * 2) * (numero2/2)
print("\nO produto do dobro do primeiro com metade do segundo: ", produto)

soma = (numero1 * 3) + numero3
print("A soma do triplo do primeiro com o terceiro. ", soma)

potencia = numero3 ** 3
print("O terceiro elevado ao cubo. ", potencia)