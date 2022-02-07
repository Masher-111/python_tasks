#Задать массив из 12 элементов, заполненных числами из [0,9]. 
# Найти сумму положительных/отрицательных элементов массива
from  random import randint
def create_list (size, start, finish):
    list = [randint(start, finish) for _ in range (size)]
    negative = sum(i for i in list if i > 0)
    positive = sum(i for i in list if i < 0)
    return list, positive, negative
print (create_list(12, -9, 9))


