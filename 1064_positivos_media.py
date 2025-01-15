'''Read 6 values that can be floating point numbers. After, print how many of them were positive. In the next line, print the average of all positive values typed, with one digit after the decimal point.

Input
The input consist in 6 numbers that can be integer or floating point values. At least one number will be positive.

Output
The first output value is the amount of positive numbers. The next line should show the average of the positive value ​typed.'''
positives=0
average=0
for i in range(6):
    n=float(input())
    if n>0:
        positives+=1
        average+=n
average/=positives
print(f"{positives} valores positivos")
print(f"{average:.1f}")

