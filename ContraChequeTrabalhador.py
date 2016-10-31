"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos
dê:
* salário bruto.
* quanto pagou ao INSS.
* quanto pagou ao sindicato.
* o salário líquido.
* calcule os descontos e o salário líquido, conforme a tabela abaixo:

Salário Bruto : R$
IR (11%) : R$
INSS (8%) : R$
Sindicato ( 5%) : R$
Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido."""

#autor: @fharaujo
#data: 28/10/2016
#Projeto: APrendendo Python - Estrutura Sequencial

IR = 11
INSS = 8
SIND = 5

salario_hora = float(input("Quanto você ganha por hora?: "))

hora_trabalhada = int(input("Digite a quantidade de horas trabalhadas mensal: "))

salario_bruto = salario_hora * hora_trabalhada
print("\nSeu salário bruto: R$ %.2f" % salario_bruto)

descontos = IR + INSS + SIND
salario_liquido = salario_bruto - (salario_bruto * descontos/100)
print("Seu salário líquido: R$ %.2f" % salario_liquido)


valor_inss = salario_bruto - (salario_bruto - (salario_bruto * INSS/100))
valor_ir =  salario_bruto - (salario_bruto - (salario_bruto * IR/100))
valor_sind =  salario_bruto - (salario_bruto - (salario_bruto * SIND/100))
print("Contribuição do INSS: R$ %.2f" % valor_inss )
print("Você pagou de Imposto de Renda: R$ %.2f" % valor_ir)
print("Sua Contribuição Sindical: R$ %.2f" % valor_sind)