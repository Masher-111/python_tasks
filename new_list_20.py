# Определить, присутствует ли в заданном списке строк, некоторое число 
import numbers


list = ['asd', 'a5k', '6', '50']

def find (arr, n):
    string = ''.join(arr)
    return str(n) in string
   
print(find(list, 6))