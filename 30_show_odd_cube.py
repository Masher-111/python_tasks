#Показать кубы чисел, заканчивающихся на четную цифру
def show_odd_cubes (x):
    list = [i**3 for i in range(0, x+1, 2)]
    return list
print (show_odd_cubes(25))
    