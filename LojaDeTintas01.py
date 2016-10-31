"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3
metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao
usuário a quantidades de latas de tinta a serem compradas e o preço total."""

#autor: @fharaujo
#data: 28/10/2016
#Projeto: APrendendo Python - Estrutura Sequencial

preco = 80
area = int(input("Digite o tamanho do local em metros²: "))

if area % 54 == 0:
    latas = area // 54
else:
    latas = area // 54 + 1

valor = latas * preco

print("Serão necessárias %i latas e o valor é: R$ %.2f" % (latas, valor))