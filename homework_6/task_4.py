my_list = list(map(int, input('Заполните лист числами через запятую: ').split(',')))
print(sum(my_list[1::2]))