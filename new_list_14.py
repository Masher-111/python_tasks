#Подсчитать сумму цифр в вещественном числе.
def sum_of_digit (n):
    Number_string = str(n).replace('.', '')
    count_number = map(int, list(Number_string))
    return sum(count_number) 

print(sum_of_digit(23.458))