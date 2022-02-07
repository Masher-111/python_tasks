# Найти сумму чисел одномерного массива стоящих на нечетной позиции
def no_odd_element (arr):
    sum = 0
    for i in arr:
        if i%2 !=0: sum = sum + arr[i]
    return sum
list = [1, 2, 3, 4, 5, 6]
print (no_odd_element(list))