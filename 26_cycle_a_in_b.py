#Возведите число А в натуральную степень B используя цикл
def cycle_a_in_b (a, b):
    result = a
    while b-1 > 0:
        b = b - 1
        result = result * a
    return result
    
print(cycle_a_in_b(2, 4))