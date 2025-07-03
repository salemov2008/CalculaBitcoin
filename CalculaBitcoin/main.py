def telaInicial():
    print("Vidente de rendimento de Bitcoin")

def calculadora():
    parcela = float(input("Aporte mensal: "))
    meses = int(input("Meses: "))
    return parcela, meses

def resultado(parcela, meses):
    resultado = parcela * meses
    print(f"{resultado:.2f}")
    return resultado

telaInicial()
parcela, meses = calculadora()
resultado(parcela, meses)