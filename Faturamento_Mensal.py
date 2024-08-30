faturamento_mensal = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

faturamento_total = sum(faturamento_mensal.values())


percentuais_por_estado = {estado: (faturamento / faturamento_total) * 100 for estado, faturamento in faturamento_mensal.items()}


for estado, percentual in percentuais_por_estado.items():
    print(f'{estado}: {percentual:.2f}%')