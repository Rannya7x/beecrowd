'''Make a program that reads five integer values. Count how many   of these values are even, odd, positive and negative. Print these information like following example.

Input
The input will be 5 integer values.

Output
Print a message like the following example with all letters in lowercase, indicating how many of these values ​​are even, odd, positive and negative.'''
even=0
odd=0
positive=0
negative=0
for i in range(5):
    n=int(input())
    if n>0:
        positive+=1
    elif n<0:
        negative+=1
    if n%2==0:
        even+=1
    else:
        odd+=1
print(f"{even} valor(es) par(es)")
print(f"{odd} valor(es) impar(es)")
print(f"{positive} valor(es) positivo(s)")
print(f"{negative} valor(es) negativo(s)")