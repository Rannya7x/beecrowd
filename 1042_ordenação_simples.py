'''Read three integers and sort them in ascending order. After, print these values in ascending order, a blank line and then the values in the sequence as they were readed.

Input
The input contains three integer numbers.

Output
Present the output as requested above.

'''
a,b,c=map(int, input().split())
lista=[a,b,c]
troca = 1
while troca:
    troca=0
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux
            troca = 1
for i in lista:
    print(i)
print()
print(a)
print(b)
print(c)