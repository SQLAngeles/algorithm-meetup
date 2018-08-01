def insertion(arr):
    for i in range(1, len(arr)):
        while arr[i-1] > arr[i] and i > 0:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1
    return arr


print(insertion([4,2,1,7,2,1,2,3,5,83,2,3,5,5]))