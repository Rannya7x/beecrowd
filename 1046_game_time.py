'''Read the start time and end time of a game, in hours. Then calculate the duration of the game, knowing that the game can begin in a day and finish in another day, with a maximum duration of 24 hours. The message must be printed in portuguese “O JOGO DUROU X HORA(S)” that means “THE GAME LASTED X HOUR(S)”

Input
Two integer numbers representing the start and end time of a game.

Output
Print the duration of the game as in the sample output.'''

for i in range(3):
    start, stop=map(int, input().split())

    def modulo(x,y):
        if x-y < 0:
            return (x-y)*(-1)

    if start < stop:
        horas = stop - start
    elif start > stop:
        horas = (modulo(start,24)) + stop
    else:
        horas=24
    print(f"O JOGO DUROU {horas} HORA(S)")