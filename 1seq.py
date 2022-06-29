count_elm = int(input('Введите количество элементов :'))
list_numbers = []
for i in range(count_elm):
    number = int(input('Введите число :'))
    list_numbers.append(number)
list_numbers.sort()
print(list_numbers)