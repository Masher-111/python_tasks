def recursionSum(array):
  if array == []:
      return 0
  return array[0] + recursionSum(array[1:])

my_list = [1, 3, 2, 0, 4]
print (recursionSum(my_list))
    
