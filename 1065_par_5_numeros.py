'''
Make a program that reads five integer values. Count how many of these values ​​are even and  print this information like the following example.

Input
The input will be 5 integer values.

Output
Print a message like the following example with all letters in lowercase, indicating how many even numbers were typed.'''
even=0
for i in range(5):
    n=int(input())
    if n%2==0:
        even+=1
print(f"{even} valores pares")