import random


turn = lambda q: q+1 if q == 0 else q-1

def Game(q, Players, level, count=221):
    if count > 0:
        print('Конфет осталось:', count)
        N = move(Players[q], level, count)
        q = turn(q)
        return Game(q, Players,level, count-N)         
    else:
        if q == 0:
            return Players[1]
        else:
            return Players[0]

def ProBOT(count):
    if count > 85:
        N = 28
    else:
        if count > 57:
            N = 1
        else:
            if count > 29:
                N = count - 29
            else: N = 28
    return N

def move(Player,level, cound):
    if Player != 'БОТ':
        p = False
        while p != True:
            print(Player, ', сколько вы хотите взять конфет?(не больше 28)')
            N = int(input())
            if N < 29 and N > 0:
                p = True
            else:
                print('Введите корректное число кофет.')
    else:
        print('Ходит БОТ:')
        if level =='нет':
            N = random.randrange(1,29)  
        else: 
            N = ProBOT(cound)
        print(N)
    return int(N)