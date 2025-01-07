n=int(input())
for i in range(n):
    numero=float(input())
    intervalos=[0,25.00001,50.00000001,75.00000001,100] #lista dos limites superiores
    if numero < 0 or numero > 100:
        print("Fora de intervalo")
    else:
        for i in range(1, len(intervalos)):#iteração sobre os indices
            if numero <= intervalos[i]:
                intervalo_final = intervalos[i]
                intervalo_inicial = intervalos[i-1]
                break
        if numero <= 25:    
            print(f"Intervalo [{intervalo_inicial:.0f},{intervalo_final:.0f}]")
        else:
            print(f"Intervalo ({intervalo_inicial:.0f},{intervalo_final:.0f}]")


