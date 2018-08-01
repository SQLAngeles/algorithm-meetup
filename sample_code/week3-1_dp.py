# Memoization: O(N)
def max_sub(arr):
    tm = float('-inf')
    cm = 0
    for i in range(1, len(arr)):
        cm += (arr[i] - arr[i-1])
        # print(cm, tm, max(cm, tm))
        tm = max(cm, tm)
        if cm < 0:
            cm = 0
    print(tm)

max_sub([100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97])
