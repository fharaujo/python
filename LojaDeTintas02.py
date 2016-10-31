"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6
metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em
galões de 3,6 litros, que custam R$ 25,00.
•Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços
em 3 situações:
•comprar apenas latas de 18 litros;
•comprar apenas galões de 3,6 litros;
•misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e
sempre arredonde os valores para cima, isto é, considere latas cheias."""

#autor: @fharaujo
#data: 29/10/2016
#Projeto: APrendendo Python - Estrutura Sequencial

area = int(input("Digite a area a ser pintada em m²: "))

print(" Digite (L) para latas, (G) para galões e (M) misturado")

escolha = input("\nQual a sua escolha: ")
valor_lata = 80
valor_galoes = 25
litro = area/6
tamanho_lata = 18
tamanho_galao = 3.6
area_total_galao = 21.4
area_total_latas = 108
folga = 1.1

if escolha == 'L' or escolha == 'l':
    if area % area_total_latas == 0:
        quant_latas = area // area_total_latas
    else:
        quant_latas = area // area_total_latas + 1
    valor = quant_latas * valor_lata
    print(" %i latas e valor R$ %i" % (quant_latas, valor))

elif escolha == 'G' or escolha == 'g':
    if area % area_total_galao == 0:
        quant_galoes = area // area_total_galao
    else:
        quant_galoes = area // area_total_galao + 1
    valor = quant_galoes * valor_galoes
    print(" %i galão(ões) e valor R$ %i" % (quant_galoes, valor))

elif escolha == 'M' or escolha == 'm':
    if area % area_total_latas == 0 and area % area_total_galao == 0:
        quant_latas = area // area_total_latas
        quant_galoes = area // area_total_galao
        total = quant_latas + quant_galoes
        valor_total = (quant_latas * valor_lata ) + (quant_galoes * valor_galoes) * folga
        print(quant_latas, quant_galoes, total, valor_total)
    else:
        quant_latas = area // area_total_latas + 1
        quant_galoes = area // area_total_galao
        total = quant_latas + quant_galoes
        valor_total = (quant_latas * valor_lata) + (quant_galoes * valor_galoes) * folga
    print("\nQuantidade de %i lata(s) e de %i galão(ões) / %i no total" % (quant_latas, quant_galoes, total))
    print("Valor à pagar: R$ %.2f" % valor_total)
else:
    print("Digite uma escolha válida!")