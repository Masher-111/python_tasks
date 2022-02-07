#Найти максимальное из трех чисел
def max_from_three (x, y, z):
    max = x
    if max < y: max = y
    if max < z: max = z
    return max
print(max_from_three(7, 9, 25))
