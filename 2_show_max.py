#Даны два числа. Показать большее и меньшее число
def show_max(a, b):
    if a > b: 
        max = a 
        min = b
    else:
        max = b 
        min = a
    return 'max ',  max, 'min ', min
print(show_max(5,9))

