# brute force: O(N^2)
def max_sub(arr):
    tm = 0
    for i in range(1, len(arr)):
        cm = 0
        for j in range(i, len(arr)):
            cm += arr[j] - arr[j-1]
            # print(cm, tm, arr[j], arr[j-1])
            if (cm > tm):
                tm = cm
    print(tm)

max_sub([100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97])
