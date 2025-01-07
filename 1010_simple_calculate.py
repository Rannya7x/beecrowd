'''
In this problem, the task is to read a code of a product 1, the number of units of product 1, the price for one unit of product 1, the code of a product 2, the number of units of product 2 and the price for one unit of product 2. After this, calculate and show the amount to be paid.

Input
The input file contains two lines of data. In each line there will be 3 values: two integers and a floating value with 2 digits after the decimal point.

Output
The output file must be a message like the following example where "Valor a pagar" means Value to Pay. Remember the space after ":" and after "R$" symbol. The value must be presented with 2 digits after the point.
'''
#recebe varios valores separados por espaço na mesma linha
n=int(input())
for i in range(n):
    produto1, unidades1, precoUnidade1 = input().split()
    produto1=int(produto1)
    unidades1=int(unidades1)
    precoUnidade1=float(precoUnidade1)
    produto2, unidades2, precoUnidade2 = input().split()
    produto2=int(produto2)
    unidades2=int(unidades2)
    precoUnidade2=float(precoUnidade2)

    total= (unidades1*precoUnidade1)+(unidades2*precoUnidade2)

    print(f"VALOR A PAGAR: R$ {total:.2f}")

# %%
produto1, unidades1, precoUnidade1 = input().split()

produto2, unidades2, precoUnidade2 = input().split()

total= (int(unidades1)*float(precoUnidade1))+(int(unidades2)*float(precoUnidade2))

print(f"VALOR A PAGAR: R$ {total:.2f}")
# %%
