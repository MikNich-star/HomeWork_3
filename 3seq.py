count_first = input('Введите элементы 1-го списка :')
numbers_first = count_first.split(',')
count_second = input('Ведите элементы 2-го списка :')
numbers_second = count_second.split(',')
res_list = []
for i in numbers_first:
    if i not in numbers_second:
        res_list.append(i)
print(res_list)
