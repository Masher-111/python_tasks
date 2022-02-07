#Найти расстояние между точками в пространстве 2D/3D
def find_distance (x1, y1, x2, y2):
    return pow((x2 - x1)**2 + (y2 - y1)**2, 0.5)

print(find_distance(0.5, 1, 3.5, 1))

def find_distance_3d (x1, y1, z1, x2, y2, z2):
    return pow((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2, 0.5)

print(find_distance_3d(0.5, 1, 2, 3.5, 1, 2))