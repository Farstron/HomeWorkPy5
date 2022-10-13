import random
import fun


ch = input('Хотите играть с ботом?(да/нет)')
if ch =='да':
    Names = ['БОТ']
    Names.append(input('Введите именя игрока:'))
    level = input('Хотите включить сложного бота?(да/нет)')
else:
    Names = input('Введите имена игроков через пробел:').split()
    level = ' '
q = random.randrange(0,2)
print('Проходит жеребьёвка....')
if q == 0:
    print('Первым ходит:', Names[0])
else: 
    print('Первым ходит:', Names[1])
Win = fun.Game(q, Names, level)
print('Победил:', Win)