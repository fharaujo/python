# Calculando o os gastos da energia elétrica em sua determinada faixa de kilowatts

#autor: @fharaujo
#data: 28/10/2016
#Projeto: APrendendo Python - Estrutura Sequencial

print( "\n"+ "*"* 50 + "")
print("  CALCULAR PAGAMENTO DE FORNECIMENTO DE ENERGIA")
print("*"* 50 + "\n")

print("Digite 'R' ou 'r' para Residência\n" +
      "Digite 'C' ou 'c' para Comércio\n" +
      "Digite 'I' ou 'i' Para Indústria\n")

option = input("Digite sua oção: ")
kiloWatts = float(input("Digite a quantidade de kiloWhats gastos: "))


if option == "R" or option == "r":
    if kiloWatts <=500:
        taxa = 0.40
        valorConta = kiloWatts * taxa
        print("O valor da taxa R$ %.2f "%taxa + "centavos")
        print("Sua débito atual para pagamento: R$ %.2f "%valorConta + "reais")
    else:
        taxa = 0.65
        valorConta = kiloWatts * taxa
        print("O valor da taxa R$ %.2f "%taxa + "centavos")
        print("Sua débito atual para pagamento: R$ %.2f "%valorConta + "reais")
elif option ==  "C" or option == "c":
    if kiloWatts <= 1000:
        taxa = 0.55
        valorConta = kiloWatts * taxa
        print("O valor da taxa R$ %.2f "%taxa + "centavos")
        print("Sua débito atual para pagamento: R$ %.2f "%valorConta + "reais")
    else:
        taxa = 0.60
        valorConta = kiloWatts * taxa
        print("O valor da taxa R$ %.2f "%taxa + "centavos")
        print("Sua débito atual para pagamento: R$ %.2f "%valorConta + "reais")
elif option == "I" or option == "i":
    if kiloWatts <=5000:
        taxa = 0.55
        valorConta = kiloWatts * taxa
        print("O valor da taxa R$ %.2f "%taxa + "centavos")
        print("Sua débito atual para pagamento: R$ %.2f "%valorConta + "reais")
    else:
        taxa = 0.60
        valorConta = kiloWatts * taxa
        print("O valor da taxa R$ %.2f "%taxa + "centavos")
        print("Sua débito atual para pagamento: R$ %.2f "%valorConta + "reais")
else:
    print("Digite um valor válido!")
