'''Read three point floating values (A, B and C) and verify if is possible to make a triangle with them. If it is possible, calculate the perimeter of the triangle and print the message:


Perimetro = XX.X


If it is not possible, calculate the area of the trapezium which basis A and B and C as height, and print the message:


Area = XX.X

Input
The input file has tree floating point numbers.

Output
Print the result with one digit after the decimal point.'''
for i in range(3):
    a,b,c=map(float, input().split())

    def modulo(x,y):
        absoluto = x-y
        if x-y < 0:
            absoluto = (x-y)*(-1)
        return absoluto

    def calculaTriangulo(a,b,c):
        booleano=True
        
        if not (modulo(b,c) < a < b + c):
            booleano = False
        if not (modulo(a,c) < b < a + c):
            booleano = False
        if not (modulo(a,b) < c < a + b):
            booleano = False
        return booleano

    def areaTrapezio(a,b,c): 
        return ((a+b)/2)*c  

    triangulo = calculaTriangulo(a,b,c)

    if triangulo:
        perimetro= a+b+c
        print(f"Perimetro = {perimetro:.1f}")
    else:
        area = areaTrapezio(a,b,c)
        print(f"Area = {area:.1f}")

