# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите натуральное число (1...N): '))

main_n = n
list_on_factor = []
num_factor = 2 

while n > 1:
    if n % num_factor == 0:
        list_on_factor.append(num_factor)
        n = int(n / num_factor)
    else:
        num_factor += 1

print(f'\n{main_n} = ', end='')
print(*list_on_factor, sep=' * ')