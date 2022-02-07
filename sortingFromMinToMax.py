def findSmallest(arr):
  smallest = arr[0]
  smallestIndex = 0
  for i in range (1, len(arr)):
    if arr[i] < smallest:
        smallest = arr[i]
        smallestIndex = i
  return smallestIndex
def selectionSort(arr):
  newArr = []
  for i in range (len(arr)):
      small = findSmallest(arr)
      newArr.append(arr.pop(small))
  return newArr

print (selectionSort([5, 0, 15, 24, 8, 6, 2]))
      
  

        