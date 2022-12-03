# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# - [2, 3, 4, 5, 6] => [12, 15, 16];


num_list = [2, 3, 4, 5, 6]
result_list = []
for i in range(int(len(num_list) / 2) + 1):
    result_list.append(num_list[i] * num_list[-i - 1])
print(result_list)






