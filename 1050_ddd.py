'''Read an integer number that is the code number for phone dialing. Then, print the destination according to the following table:

DDD Destination
61  Brasilia
71  Salvador
11  Sao Paulo
21  Rio de Janeiro
32  Juiz de Fora
19  Campinas
27  Vitoria
31  Belo Horizonte


If the input number isn’t found in the above table, the output must be:
DDD nao cadastrado
That means “DDD not found” in Portuguese language.

Input
The input consists in a unique integer number.

Output
Print the city name corresponding to the input DDD. Print DDD nao cadastrado if doesn't exist corresponding DDD to the typed number.'''

ddd=int(input())

tabela={
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"
}

try:
    print(tabela[ddd])
except KeyError:
    print("DDD nao cadastrado")