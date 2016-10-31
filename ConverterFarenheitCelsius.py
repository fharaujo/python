"""Faça um Programa que peça a temperatura em graus Farenheit,
transforme e mostre a temperatura em graus Celsius.
•C = (5 * (F-32) / 9)."""

#autor: @fharaujo
#data: 28/10/2016
#Projeto: APrendendo Python - Estrutura Sequencial

fahrenheit = int(input("Digite a temperatura em Fahrenheit: "))
celsius = (5 * (fahrenheit - 32)/9)
print("A temperatura em Celsius: ",celsius)