def binary_search(list, item):
    low = 0
    high = len(list) -1

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item :
            high = mid -1
        else:
            low = mid + 1
    return None
my_list = [1,4,9,13,23,28,31,56,60,78,89,94,99]
print(binary_search(my_list,31))
