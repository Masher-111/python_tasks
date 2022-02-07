#Написать программу получающую набор произведений чисел от 1 до N.
#Пример: пусть N = 4, тогда
#[ 1, 2, 6, 24 ]

def mult (n):
    list = [0] * n
    result = 1
    for i in range (1, n+1):
        result = result * i
        list[i-1] = result
    return list
    