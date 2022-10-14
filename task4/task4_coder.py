# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных
# Модуль сжатия
from functools import reduce

def coder(word):
    count = 1
    res = ' '
    for i in range(1,len(WORD)):
        if WORD[i] == WORD[i-1]:
            count += 1
        else: 
            co=str(count)
            res+=co+' '+WORD[i-1]+' '
            count = 1
    return res+str(count)+' '+WORD[len(WORD)-1]
with open('code_word.txt','r') as data:
    WORD = data.readline()
with open('code.txt','w') as code:
    code.write(coder(WORD))
