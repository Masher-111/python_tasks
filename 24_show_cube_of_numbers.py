#Найти кубы чисел от 1 до N
def show_cube_of_numbers (n):
    array = [i**3 for i in range(1, n+1)]
    return array
print (show_cube_of_numbers(5))

