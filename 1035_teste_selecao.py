'''Read 4 integer values A, B, C and D. Then if B is greater than C and D is greater than A and if the sum of C and D is greater than the sum of A and B and if C and D were positives values and if A is even, write the message “Valores aceitos” (Accepted values). Otherwise, write the message “Valores nao aceitos” (Values not accepted).

Input
Four integer numbers A, B, C and D.

Output
Show the corresponding message after the validation of the values​​.'''

a,b,c,d=map(int, input().split())

if a % 2 == 0:
    if c >= 0 and d >= 0: 
        if (c+d) > (a+b):
            if b > c and d > a:
                print("Valores aceitos")
else:
    print("Valores nao aceitos")
