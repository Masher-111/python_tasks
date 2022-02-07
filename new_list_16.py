#Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму
def array_create (n):
  return [((1 + 1/i)**i) for i in range (1, n+1)]
print(array_create(4))
def recursionSum(array):
    if array == []: return 0
    return array[0] + recursionSum(array[1:])  

print (recursionSum(array_create (3)))
        

