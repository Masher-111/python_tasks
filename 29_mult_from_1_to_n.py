#Написать программу вычисления произведения чисел от 1 до N
def mult_from_1_to_n (n):
    if n == 1: return 1
    return mult_from_1_to_n(n-1) * n
print(mult_from_1_to_n(4))
    