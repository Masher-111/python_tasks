#Показать вторую цифру трёхзначного числа
def show_second_number(x):
    x = round((x % 100 - x % 10)/10)
    
    print(x)
show_second_number(845)