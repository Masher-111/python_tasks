#В двумерном массиве заменить элементы, у которых оба индекса чётные на их квадраты
def fill_matrix (array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if i%2==0==j%2: array[i][j] = array[i][j]**2
    return array

matrix = [[1, 2, 3], [2, 2, 2], [23, 1, 3]]
print(fill_matrix(matrix))