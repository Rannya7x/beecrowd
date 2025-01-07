'''Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in hours:minutes:seconds.

Input
The input file contains an integer N.

Output
Print the read time in the input file (seconds) converted in hours:minutes:seconds like the following example.'''

n=int(input())
for i in range(n):
    segundos=int(input())
    horas=segundos//3600
    minutos=(segundos//60)%60
    segundos=segundos%60
    print(f"{horas}:{minutos}:{segundos}")