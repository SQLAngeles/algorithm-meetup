def selection(arr):
    for i in range(len(arr)):
        mi = i
        for j in range(i, len(arr)):
        	if arr[mi] > arr[j]:
        		mi = j
        arr[i], arr[mi] = arr[mi], arr[i]
    return arr


print(selection([4,2,1,7,2,1,2,3,5,83,2,3,5,5]))