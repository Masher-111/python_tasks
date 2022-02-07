#Задать массив из 8 элементов, заполненных нулями и единицами вывести их на экран
from  random import randint
def create_list (size, start, finish):
    list = [randint(start, finish) for _ in range (size)]
    return list
print (create_list(8, 0, 1))

