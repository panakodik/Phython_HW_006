# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


# a1 = int(input("Введите первый элемент прогрессии: "))
# d = int(input("Введите разность: "))
# n = int(input("Введите количество элементов: "))

# progression = [a1 + (i * d) for i in range(n)]

# print("Элементы прогрессии:")
# for element in progression:
#     print(element)




# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_indexes(array, min_value, max_value):
    indexes = []
    for i, value in enumerate(array):
        if min_value <= value <= max_value:
            indexes.append(i)
    return indexes

my_list = [1, 9, 3, 0, 2, 5, 4, 8]
min_value = 5
max_value = 9
result = find_indexes(my_list, min_value, max_value)
print(result)
