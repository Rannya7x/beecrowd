'''
Using the following table, write a program that reads a code and the amount of an item. After, print the value to pay. This is a very simple program with the only intention of practice of selection commands.



Input
The input file contains two integer numbers X and Y. X is the product code and Y is the quantity of this item according to the above table.

Output
The output must be a message "Total: R$ " followed by the total value to be paid, with 2 digits after the decimal point.'''
# %%
x,y = map(int, input().split())
lanches={
    "1": 4,
    "2": 4.5,
    "3": 5,
    "4": 2,
    "5": 1.5  
}
valor = 0
for i in lanches:
    if x == float(i):
        preco = lanches[f"{x}"]
        valor += (y*preco)

print(f"Total: R$ {valor:.2f}")
