#Найти третью цифру числа или сообщить, что её нет
def show_third(x):
    str_x = str(x)
    if len(str_x) > 2: return str_x[2]
    else: return False


print(show_third(235698))
    
    
    