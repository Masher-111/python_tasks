#Показать первую цифру дробной части числа

def first_figure (x):
    return int((x*10) % 10)
print(first_figure(10022.58))
