# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных
# Модуль восстановления данных
def decoder(word):
    i = 1
    res = ''
    while i < len(word):
        for j in range(0,int(word[i-1])):
            res += word[i]
        i+=2
    return res

with open('code.txt','r') as code:
    WORD = code.readline().split()

with open('decode.txt','w') as decode:
    decode.write(decoder(WORD))