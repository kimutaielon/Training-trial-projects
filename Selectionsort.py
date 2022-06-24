def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(0,len(arr)):
        if arr[i] < smallest:
            Smallest = arr[i]
            smallest_index = i
    return smallest_index
def SelectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr
print(SelectionSort([5,45,34,70,245,700,456,390,378,569,13265,432,79,67,90,85]))