
numbers = input('Введите любые числа через запятую :')
list_numbers = numbers.split(',')
res_list = []
for i in list_numbers:
    if i not in res_list:
        res_list.append(i)
print(res_list)

                       # Tак еще можно :
import numpy as np
numbers = input('Введите любые числа через запятую :')
list_numbers = numbers.split(',')
res_list = np.array(list_numbers)
unique_list = np.unique(res_list)
print(unique_list)