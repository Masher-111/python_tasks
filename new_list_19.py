#Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел
import datetime
def get_random ():
    return datetime.datetime.now().microsecond%10
n = get_random()
print(n)
