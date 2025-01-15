'''Read an integer N. This N will be the number of integer numbers X that will be read.

Print how many these numbers X are in the interval [10,20] and how many values are out of this interval.
 

Input
The first line of input is an integer N (N < 10000), that indicates the total number of test cases.
Each case is an integer number X (-107 < X < 107).

 

Output
For each test case, print how many numbers are in and how many values are out of the interval'''

n=int(input())
inn=0
out=0
for i in range(n):
    n=int(input())
    if 10<=n<=20:
        inn+=1
    else:
        out+=1
print(f"{inn} in")
print(f"{out} out")