# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных
# модуль создания кодового слова
import random
G=lambda alf: alf[random.randrange(0,len(alf))]

def code_word():
    alf = 'AB'
    out_list = [G(alf) for i in range(0,20)]
    return ''.join(out_list)

with open('code_word.txt','w') as word:
    word.write(code_word())

def coder(word):
    count = 0
    res = ''
    for i in word:
        if i == res[len(res)-1]:
            count += 1
        else: res += str(count) + i
    return res
