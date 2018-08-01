# divide and conquer: O(NlgN)
def max_crossing_sum(arr, l, m, h) :
    sm = 0 
    left_sum = float('-inf')
     
    for i in range(m, l-1, -1) :
        sm = sm + arr[i]
        if (sm > left_sum) :
            left_sum = sm
    sm = 0
    right_sum = float('-inf')
    for i in range(m + 1, h + 1) :
        sm = sm + arr[i]
        if (sm > right_sum) :
            right_sum = sm
    return left_sum + right_sum;
 
def max_sub_array_sum(arr, l, h) :
    if (l == h) :
        return arr[l]
    m = (l + h) // 2
    # print(m, l, h)
    return max(max_sub_array_sum(arr, l, m),
               max_sub_array_sum(arr, m+1, h),
               max_crossing_sum(arr, l, m, h))

def max_sub(arr):
    arr = [arr[i]-arr[i-1] for i in range(len(arr))]
    print(arr)
    print(max_sub_array_sum(arr, 0, len(arr)-1))

max_sub([100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97])
