'''Read a value of floating point with two decimal places. This represents a monetary value. After this, calculate the smallest possible number of notes and coins on which the value can be decomposed. The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. Print the message “NOTAS:” followed by the list of notes and the message “MOEDAS:” followed by the list of coins.

Input
The input file contains a value of floating point N (0 ≤ N ≤ 1000000.00).

Output
Print the minimum quantity of banknotes and coins necessary to change the initial value, as the given example.'''
# %%
n=int(input())
for i in range(n):
    valor=float(input())
    notas100=valor//100
    resto100=valor%100
    notas50=resto100//50
    resto50=resto100%50
    notas20=resto50//20
    resto20=resto50%20
    notas10=resto20//10
    resto10=resto20%10
    notas5=resto10//5
    resto5=resto10%5
    notas2=resto5//2
    resto2=resto5%2
    #Moedas
    moedas=valor%1
    moedas1=resto2//1
    moedas050=moedas//0.50
    resto050=moedas%0.50
    moedas025=resto050//0.25
    resto025=resto050%0.25
    moedas010=resto025//0.10
    resto010=resto025%0.10
    moedas005=resto010//0.05
    resto005=resto010%0.05
    moedas001=resto005//0.01
    print("NOTAS:")
    print(f"{notas100:.0f} nota(s) de R$ 100.00")
    print(f"{notas50:.0f} nota(s) de R$ 50.00")
    print(f"{notas20:.0f} nota(s) de R$ 20.00")
    print(f"{notas10:.0f} nota(s) de R$ 10.00")
    print(f"{notas5:.0f} nota(s) de R$ 5.00")
    print(f"{notas2:.0f} nota(s) de R$ 2.00")
    print("MOEDAS:")
    print(f"{moedas1:.0f} moeda(s) de R$ 1.00")
    print(f"{moedas050:.0f} moeda(s) de R$ 0.50")
    print(f"{moedas025:.0f} moeda(s) de R$ 0.25")
    print(f"{moedas010:.0f} moeda(s) de R$ 0.10")
    print(f"{moedas005:.0f} moeda(s) de R$ 0.05")
    print(f"{moedas001:.0f} moeda(s) de R$ 0.01")
# %%

