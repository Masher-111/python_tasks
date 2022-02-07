#Задать массив из 8 элементов и вывести их на экран
from  random import randint
def create_list (size, start, finish):
    list = [randint(start, finish) for _ in range (size)]
    return list
print (create_list(8, -20, 20))

import random
array = random.sample(range(0, 100), 8)
print(array)

