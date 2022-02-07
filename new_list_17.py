#17.	Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

n=4
my_arr = [i for i in range (-n, n+1)]
lines = [str(i) for i in range(0, (n*2)+1)]

with open(r"test.txt", "w") as file:
    for  line in lines:
        file.write(line + '\n')
        





     