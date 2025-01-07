'''Read the start time and end time of a game, in hours and minutes (initial hour, initial minute, final hour, final minute). Then print the duration of the game, knowing that the game can begin in a day and finish in another day,

Obs.: With a maximum game time of 24 hours and the minimum game time of 1 minute.

Input
Four integer numbers representing the start and end time of the game.

Output
Print the duration of the game in hours and minutes, in this format: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” . Which means: the game lasted XXX hour(s) and YYY minutes.'''
for i in range(3):
    start, minStart, stop, minStop=map(int, input().split())

    inicio = (start*60)+minStart
    fim = (stop*60)+minStop

    if inicio == fim:
        horas = 24
        minutos = 0
    elif inicio < fim:
        minutosJogados = fim - inicio
        horas = minutosJogados // 60
        minutos = minutosJogados % 60
    else:
        minutosJogados = (fim + (24*60)) - inicio
        horas = minutosJogados // 60
        minutos = minutosJogados % 60

    print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")