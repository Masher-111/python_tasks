#Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
#Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
def dictionary (n):
    dict = {}
    for i in range (1, n):
        j = str(3*i +1)
        dict[i] = j
    return dict

print(dictionary(8))

        
        
    
       
    
    
