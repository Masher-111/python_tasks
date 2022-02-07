#Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
def show_biggest_number (x):
    a = x//10
    b = x%10
    if a > b: return(a)
    else: return(b)
print(show_biggest_number(63))
