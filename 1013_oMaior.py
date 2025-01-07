'''Make a program that reads 3 integer values and present the greatest one followed by the message "eh o maior". Use the following formula:



Input
The input file contains 3 integer values.

Output
Print the greatest of these three values followed by a space and the message “eh o maior”.'''

n=int(input())
for i in range(n):
    A,B,C=map(int, input().split())
    maiorAB = (A+B+abs(A-B))//2 #maiorDe2Numeros
    if maiorAB >= C:
        print(f"{maiorAB} eh o maior")
    else:{
        print(f"{C} eh o maior")
    }