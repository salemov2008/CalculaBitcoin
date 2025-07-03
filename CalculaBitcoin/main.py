import requests

#essa parte peguei do GEMINI pra estudar cada parte dessa biblioteca
def obter_preco_bitcoin():
    """
    Consulta a API do CoinGecko para obter o preço atual do Bitcoin em BRL.
    Retorna o preço como float, ou None se houver um erro.
    """
    try:
        # URL da API do CoinGecko para o preço do Bitcoin em BRL
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl"

        # Faz a requisição HTTP
        response = requests.get(url)

        # Verifica se a requisição foi bem-sucedida (status code 200)
        response.raise_for_status()  # Lança um erro para status codes de erro (4xx ou 5xx)

        # Converte a resposta JSON em um dicionário Python
        data = response.json()

        # Extrai o preço do Bitcoin em BRL
        preco_bitcoin = data['bitcoin']['brl']
        return preco_bitcoin

    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar o preço do Bitcoin: {e}")
        return None
    except KeyError:
        print("Erro: Não foi possível encontrar o preço do Bitcoin na resposta da API.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None


def telainicial():                                # mensagem inicial
    print("Vidente de rendimento de Bitcoin")

def calculadora():                                 # inserção de valores
    parcela = float(input("Aporte mensal: "))
    meses = int(input("Meses: "))
    return parcela, meses

def calculo(valor1, valor2):                       # calcula
    resultado = valor1 * valor2
    print(f"{resultado:.2f}")
    return resultado

telainicial()

# Chamada da nova função para obter o preço GEMINI
preco_atual_btc = obter_preco_bitcoin()

if preco_atual_btc is not None:
    print(f"\nPreço atual do Bitcoin (BRL): R${preco_atual_btc:,.2f}")
    print("\n--- Calculadora de Rendimento ---")

    ValorParcela, QuantidadeMeses = calculadora()
    calculo(ValorParcela, QuantidadeMeses)

    # Você pode usar o preco_atual_btc aqui para cálculos mais avançados,
    # por exemplo, para estimar quantos bitcoins o usuário compraria com o aporte.

else:
    print("Não foi possível continuar sem o preço do Bitcoin.")