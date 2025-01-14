'''Peter is organizing an event in his University. The event will be in April month, beginning and finishing within April month. The problem is: Peter wants to calculate the event duration in seconds, knowing obviously the begin and the end time of the event.

You know that the event can take from few seconds to some days, so, you must help Peter to compute the total time corresponding to duration of the event.

Input
The first line of the input contains information about the beginning day of the event in the format: “Dia xx”. The next line contains the start time of the event in the format presented in the sample input. Follow 2 input lines with same format, corresponding to the end of the event.

Output
Your program must print the following output, one information by line, considering that if any information is null for example, the number 0 must be printed in place of W, X, Y or Z:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Consider that the event of the test case have the minimum duration of one minute. “dia” means day, “hora” means hour, “minuto” means minute and “Segundo” means second in Portuguese.
'''
#%%
dia_inicial=input()
hora_inicial,minuto_inicial,segundo_inicial=map(int, input().split(":"))
dia_final=input()
hora_final,minuto_final,segundo_final=map(int, input().split(":"))
dia_inicial=dia_inicial[4:]
dia_final=dia_final[4:]
#%%

segundos_iniciais=int(dia_inicial)*24*60*60 + segundo_inicial + minuto_inicial*60 + hora_inicial*60*60
segundos_finais=int(dia_final)*24*60*60 + segundo_final + minuto_final*60 + hora_final*60*60
segundos_totais=segundos_finais-segundos_iniciais

dias=segundos_totais//(24*60*60)#86400
horas=(segundos_totais%(24*60*60))//(60*60)#3600
minutos=(segundos_totais%(60*60))//60
segundos=segundos_totais%60

#%%
print(f"{dias} dia(s)")
print(f"{horas} horas(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
# %%
