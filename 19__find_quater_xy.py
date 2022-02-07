#Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0
def  quater_of_coordinate (x, y):
    if x > 0 and y > 0: return '1'
    elif x > 0 and y < 0: return '2'
    elif x < 0 and y < 0: return '3'
    else: return '4'
print(quater_of_coordinate(5, -8))