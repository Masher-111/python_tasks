#Дано число. Проверить кратно ли оно 7 и 23
def is_mult_7or_23 (x):
    return x % 7== 0 and x % 23 == 0

print (is_mult_7or_23(161))