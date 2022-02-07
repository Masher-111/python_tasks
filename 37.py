#В одномерном массиве из 123 чисел найти количество элементов из отрезка [10,99]
from  random import randint
def create_list (size, start, finish):
    list = [randint(start, finish) for _ in range (size)]
    count = 0
    for i in list: 
        if 10 < i < 99: count = count +1
    return list, count
print (create_list(123, -10, 120))