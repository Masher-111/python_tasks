#Задать номер четверти, показать диапазоны для возможных координат
def show_diapozone_of_coordinates (n):
    if n == 1: return '(0;+∞), (0;+∞)'
    elif n == 2: return '(-∞;0)","(0;+∞)'
    elif n == 3: return '(-∞;0)","(-∞;0)'
    elif n == 4: return '(0;+∞)","(-∞;0)'
print (show_diapozone_of_coordinates(4))