#Задать массив, заполнить случайными положительными трёхзначными числами. Показать количество нечетных\четных чисел
from  random import randint
def create_list (size, start, finish):
    list = [randint(start, finish) for _ in range (size)]
    count_odd = 0
    count_no_odd = 0
    for i in list: 
        if i %2== 0: count_odd = count_odd +1
        if i %2 != 0: count_no_odd = count_no_odd +1
    return list, count_odd, count_no_odd
print (create_list(10, 100, 999))


    