#Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y
def De_Morgan_low (x, y):
  return (not (x or y)) == ((not x) and (not y))

for x in range(0, 2):
    for y in range(0, 2):
        print(De_Morgan_low(x, y))