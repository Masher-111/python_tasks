#Показать таблицу квадратов чисел от 1 до N
def show_quater_of_numbers (n):
    array =[ i*i for i in range(1, n+1)]
    return array

print (show_quater_of_numbers(5))