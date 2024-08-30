import json

def analisar_faturamento(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
            faturamento_diario = dados['faturamento_diario']

        valores = [valor for valor in faturamento_diario if valor > 0]
        soma = sum(valores)
        dias_com_faturamento = len(valores)
        media = soma / dias_com_faturamento

        menor_valor = min(valores)
        maior_valor = max(valores)
        dias_acima_da_media = sum(1 for valor in valores if valor > media)

        print("Menor valor de faturamento:", menor_valor)
        print("Maior valor de faturamento:", maior_valor)
        print("Número de dias com faturamento acima da média:", dias_acima_da_media)

    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: Arquivo '{nome_arquivo}' não é um JSON válido.")
    except KeyError:
        print(f"Erro: Chave 'faturamento_diario' não encontrada no arquivo '{nome_arquivo}'.")
    except ZeroDivisionError:
        print(f"Erro: Nenhum dia com faturamento encontrado no arquivo '{nome_arquivo}'.")

analisar_faturamento("faturamento.json")