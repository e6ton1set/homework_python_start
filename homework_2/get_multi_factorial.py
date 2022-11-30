

def get_multi_factorial (num): # метод, который с помощью рекурсии находит факториал числа (1, 1*2, 1*2*3, 1*2*3*4 ... num)
    if num == 0 or num == 1:
        return 1
    else:
        return get_multi_factorial(num - 1) * num
        