def RecursionFindMax(array):
    if len(array) ==2:
        return array[0] if array[0] > array[1] else array[1]
    otherMax = RecursionFindMax(array [1:])
    return array [0] if array[0] > otherMax else otherMax

my_list = [1, 3, 21, 0, 4]
print (RecursionFindMax(my_list))