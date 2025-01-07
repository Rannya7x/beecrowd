def verificar_intervalo(numero):
    if numero < 0 or numero > 100:
        return "Fora de intervalo"
    elif numero <= 25:
        return "[0,25]"
    elif numero <= 50:
        return "(25,50]"
    elif numero <= 75:
        return "(50,75]"
    else:
        return "(75,100]"
n=int(input())
for i in range(n):
    numero = float(input())
    print(verificar_intervalo(numero))