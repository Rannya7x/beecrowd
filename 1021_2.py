n=int(input())
for i in range(n):
    valor_total=float(input())
    valor_em_centavos= int(valor_total*100)# transforma reais em centavos
    notas_moedas=[10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1] #todas em centavos

    print("NOTAS:")
    for valor in notas_moedas[:6]:
        quantidade_notas = valor_em_centavos // valor
        resto_notas = valor_em_centavos % valor
        valor_em_centavos = resto_notas
        print(f"{quantidade_notas} nota(s) de R$ {valor/100:.2f}")#transforma em reais
    print("MOEDAS:")
    for valor in notas_moedas[6:]:
        quantidade_moedas = valor_em_centavos // valor
        resto_moedas = valor_em_centavos % valor
        valor_em_centavos = resto_moedas
        print(f"{quantidade_moedas} moeda(s) de R$ {valor/100:.2f}")