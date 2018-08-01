def bubble(arr):
    for i in range(len(arr)-1):
        for x in range(len(arr)-1-i):
            if arr[x] > arr[x+1]:
                arr[x], arr[x+1] = arr[x+1], arr[x]
    return arr


print(bubble([4,2,1,7,2,1,2,3,5,83,2,3,5,5]))