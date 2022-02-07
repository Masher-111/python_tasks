#Программа проверяет пятизначное число на палиндромом.
def is_palindrom (x):
    number = str(x)
    return number[0] == number[4] and number[1] == number[3]
print (is_palindrom(56365))