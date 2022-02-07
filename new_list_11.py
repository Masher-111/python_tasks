#Для натурального N создать множество: 1, -3, 9, -27, 81 и т.д.
def show_cube_of_numbers (n):
 return {((-3)**i) for i in range(n)}
 
print (show_cube_of_numbers(5))