'''Read two integer values X and Y. Print the sum of all odd values between them.

Input
The input file contain two integer values.

Output
The program must print an integer number. This number is the sum off all odd values between both input values that must fit in an integer number.'''

x=int(input())
y=int(input())
sum=0
for i in range(y+1,x):
    if i%2!=0:
        sum+=i
print(sum)