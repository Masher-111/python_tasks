#Реализовать алгоритм перемешивания списка. 
from random import randint
my_list = [randint (-10, 10) for i in range (6)]
print (my_list)
def algoritm_Fisher_Yates (arr):
    for i in range (len(arr) -1, 0, -1):
        j = randint(0, i+1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr
print (algoritm_Fisher_Yates(my_list))