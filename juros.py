def calcular_juros_compostos():
    principal = float(input("Digite aqui o valor inicial do investimento (R$): "))
    taxa = float(input("Digite aqui a taxa de juros mensal (ex: 1.0 para 1%): "))
    tempo = int(input("Digite o tempo em meses (ex: 12): "))
    taxa_decimal = taxa / 100
    montante_final = principal * ((1 + taxa_decimal) ** tempo)
    montante_formatado = round(montante_final, 2)
    print("-" * 30)
    print(f"Valor investido (principal): R$ {principal:.2f}")
    print(f"Taxa de juros: {taxa: .2f}% a.m.")
    print(f"Periodo: {tempo} meses")
    print("-" * 30)
    print(f"Montante final após {tempo} meses: R$ {montante_formatado}")

calcular_juros_compostos()