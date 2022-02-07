def CountOfElement(array):
    if array == []:
      return 0
    return 1 + CountOfElement(array[1:])

my_list = [1, 3, 2, 0, 4]
print (CountOfElement(my_list))