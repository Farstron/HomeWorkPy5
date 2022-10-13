move = lambda t: 'x' if t == 0 else 'o'  
turn = lambda q: q+1 if q == 0 else q-1

def GameXO(q, Plaeyrs, dask,counter = 0, t = 0, w = False):
    if counter < 9 and w == False:
        p = False
        print(Plaeyrs[q], 'делайте свой ход(строка, столбец):')
        pos = input().split()
        pos[0]=int(pos[0])
        pos[1]=int(pos[1])
        while p == False:
            if dask[pos[0]][pos[1]] != ' ':
                print('Упс, эта позиция занята. Выберите другую:')
                pos = input().split()
                pos[0]=int(pos[0])
                pos[1]=int(pos[1])
            else: 
                p = True
        dask[pos[0]][pos[1]] = move(t)
        for i in range(0,3):
            print(dask[i])
        q = turn(q)
        w = win(dask, move(t))
        t = turn(t)
        return GameXO(q, Plaeyrs, dask, counter+1,t, w)
    else:
        if w == True:
            return 'Победил ' + Plaeyrs[turn(q)]
    return 'Ничья'

def win(dask, move):
    check_list = [move for n in range(0,3)]
    if check_list in dask or tuple(check_list) in list(zip(*dask)) or check_list == [dask[i][i] for i in range(0,3)] or check_list == [dask[i][len(dask)-1-i] for i in range(0,3)]:
        return True
    return False