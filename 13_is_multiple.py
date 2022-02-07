#Выяснить, кратно ли число заданному, если нет, вывести остаток.
def is_multiple (x, y):
    if x % y != 0 : return (x%y)
    return x % y == 0 
print(is_multiple(7, 2))
    
