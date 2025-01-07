'''Read 3 double numbers (A, B and C) representing the sides of a triangle and arrange them in decreasing order, so that the side A is the biggest of the three sides. Next, determine the type of triangle that they can make, based on the following cases always writing an appropriate message:

if A ≥ B + C, write the message: NAO FORMA TRIANGULO
if A2 = B2 + C2, write the message: TRIANGULO RETANGULO
if A2 > B2 + C2, write the message: TRIANGULO OBTUSANGULO
if A2 < B2 + C2, write the message: TRIANGULO ACUTANGULO
if the three sides are the same size, write the message: TRIANGULO EQUILATERO
if only two sides are the same and the third one is different, write the message: TRIANGULO ISOSCELES
Input
The input contains three double numbers, A (0 < A) , B (0 < B) and C (0 < C).

Output
Print all the classifications of the triangle presented in the input.'''

a,b,c=map(float, input().split())
lista=[a,b,c]

def ordena(lista):
    troca = 1
    while troca:
        troca = 0
        for i in range(len(lista)-1):
            if lista[i] < lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                troca = 1
    return lista

ordena(lista)
a,b,c = map(float, lista)
if a >= b+c or a<=0 or b<=0 or c<=0:
    print("NAO FORMA TRIANGULO")
else:
    if a**2 == (b**2)+(c**2):
        print("TRIANGULO RETANGULO")
    if a**2 > (b**2)+(c**2):
        print("TRIANGULO OBTUSANGULO")
    if a**2 < (b**2)+(c**2):
        print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    if (a==b and a != c) or (b==c and b != a) or (a==c and a != b):
        print("TRIANGULO ISOSCELES")