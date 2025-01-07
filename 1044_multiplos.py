'''Read two integer values (A and B). After, the program should print the message "Sao Multiplos" (are multiples) or "Nao sao Multiplos" (aren’t multiples), corresponding to the read values.

Input
The input has two integer numbers.

Output
Print the relative message to the input as stated above.'''

a,b=map(int, input().split())
if a%b == 0 or b%a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")