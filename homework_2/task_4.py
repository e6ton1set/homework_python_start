# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

num = int(input('Введите целое число N: '))

numbers = []
for i in range(-abs(num), abs(num) + 1):
    numbers.append(i)
print(numbers)

multi = 1
path = 'file.txt'
with open(path, 'r') as data:
    for line in data:
        multi *= numbers[int(line)]
        print(multi)