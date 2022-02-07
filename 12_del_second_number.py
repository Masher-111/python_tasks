#Удалить вторую цифру трёхзначного числа
def del_second_number (x):
    return (x//100 * 10) + x%10
print(del_second_number(254))
