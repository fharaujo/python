"""Faça um Programa que pergunte quanto você ganha por hora
e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês."""

#autor: @fharaujo
#data: 26/10/2016
#Projeto: APrendendo Python

salario_hora = float(input("Quanto você ganha por hora?: "))

hora_trabalhada = int(input("Digite a quantidade de horas trabalhadas mensal: "))

salario_total =salario_hora*hora_trabalhada

print("\nVocê trabalhou %i horas e seu salário: R$%.2f" % (hora_trabalhada, salario_total))
