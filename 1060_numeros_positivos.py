'''
Write a program that reads 6 numbers. These numbers will only be positive or negative (disregard null values). Print the total number of positive numbers.

Input
Six numbers, positive and/or negative.

Output
Print a message with the total number of positive numbers.'''


lista=[]
for i in range(6):
    n=float(input())
    
    if n>0:
        lista.append(n)
print(f"{len(lista)} valores positivos")