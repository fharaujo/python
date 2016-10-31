"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade
de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo
usando este link (em minutos)."""

#autor: @fharaujo
#data: 31/10/2016
#Projeto: APrendendo Python - Estrutura Sequencial

arquivo = int(input("\nDigite o tamanho em (MB) do arquivo: "))
velocidade_net = int(input("Digite a velocidade da internet em (Mbps): "))

calc_bits = arquivo * 1024
calc_net = (velocidade_net * 1024) / 8

tempo = (calc_bits / calc_net)/60
print("\nO tempo estimado em %.2f" % tempo + " minutos/seg. aproximadamente")