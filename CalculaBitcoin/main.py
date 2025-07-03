def telainicial():
    print("Vidente de rendimento de Bitcoin")

def calculadora():
    parcela = float(input("Aporte mensal: "))
    meses = int(input("Meses: "))
    return parcela, meses

def calculo(valor1, valor2):
    resultado = valor1 * valor2
    print(f"{resultado:.2f}")
    return resultado

telainicial()
ValorParcela, QuantidadeMeses = calculadora()
calculo(ValorParcela, QuantidadeMeses)