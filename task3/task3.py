import random
import fun

dask = [[' ' for n in range(0,3)]for y in range(0,3)]
Names = input('Введите имена игроков через пробел:').split()
print('Проходит жеребьёвка....')
q = random.randrange(0,2)
if q == 0:
    print('Первым ходит(x):', Names[0])
else: 
    print('Первым ходит(x):', Names[1])
print(fun.GameXO(q,Names,dask))
