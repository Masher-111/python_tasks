#В матрице чисел найти сумму элементов главной диагонали
def sum_of_element (arr):
    result = 0
    for i in range(len(arr)):
        for j in range (len(arr[i])):
            if i==j: result+= arr[i][j]
    return result

matrix = [[1, 2, 3], [2, 2, 2], [3, 3, 3]]

print(sum_of_element(matrix))