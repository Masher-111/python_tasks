#Показать четные числа от 1 до N
def show_odd (n):
  list = [i for i in range(2, n+1, 2)]
  return list

print(show_odd(6))