# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    tmp = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            tmp += txt[i]
        else:
            res = res + txt[i] * int(tmp)
            tmp = ''
    return res


s = input("Введите текст: ")
print(f"Кодированный текст: {coding(s)}")
print(f"Дешифрованный текст: {decoding(coding(s))}")