'''Read an integer value X and print the 6 consecutive odd numbers from X, a value per line, including X if it is the case.

Input
The input will be a positive integer value.

Output
The output will be a sequence of six odd numbers.'''

x=int(input())
odds=0
while odds < 6:
    if x%2!=0:
        print(x)
        x+=2
        odds+=1
    else:
        x+=1