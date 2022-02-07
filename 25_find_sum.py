#Найти сумму чисел от 1 до А
def show_sum_from_1_to_a (a):
    if a == 0: return 0
    return a + show_sum_from_1_to_a(a-1)
print(show_sum_from_1_to_a(3))

