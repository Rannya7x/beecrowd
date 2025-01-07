'''
The company ABC decided to give a salary increase to its employees, according to the following table:


Salary	            Readjustment Rate
0 - 400.00          15%
400.01 - 800.00     12%
800.01 - 1200.00    10%
1200.01 - 2000.00   7%
Above 2000.00       4%

Read the employee's salary, calculate and print the new employee's salary, as well the money earned and the increase percentual obtained by the employee, with corresponding messages in Portuguese, as the below example.
Input
The input contains only a floating-point number, with 2 digits after the decimal point.

Output
Print 3 messages followed by the corresponding numbers (see example) informing the new salary, the among of money earned (both must be shown with 2 decimal places) and the percentual obtained by the employee. Note:
Novo salario:  means "New Salary"
Reajuste ganho: means "Money earned"
Em percentual: means "In percentage"'''
for i in range(3):
    salario=float(input())

    if salario <= 400.00:
        percentual = 0.15
    elif 400.01 <= salario <= 800.00:
        percentual = 0.12
    elif 800.01 <= salario <= 1200.00:
        percentual = 0.10
    elif 1200.01 <= salario <= 2000.00:
        percentual = 0.07
    else:
        percentual = 0.04

    reajuste=salario*percentual
    novoSalario= salario + reajuste

    print(f"Novo salario: {novoSalario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual*100:.0f} %")