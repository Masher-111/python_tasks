#Подсчитать сумму цифр в числе
def sum_of_numbers (x):
    result = 0
    while x!=0:
        result += int(x%10)
        x = int(x/10)
    return result
print(sum_of_numbers(253))    