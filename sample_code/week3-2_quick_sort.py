# QUICK SORT
import sys
import random

sys.setrecursionlimit(10000)
global recursion_cnt
recursion_cnt=0

def partition(arr,low,high):
  i = low-1
  # random pivot
  # seed = random.randint(low, high)
  # arr[seed], arr[high] = arr[high], arr[seed]
  pivot = arr[high]

  for j in range(low , high):
    if arr[j] <= pivot:
      i = i+1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i+1], arr[high] = arr[high], arr[i+1]
  return i+1


def quick_sort(arr,low,high):
  global recursion_cnt
  if low < high:
    recursion_cnt += 1
    pi = partition(arr,low,high)
    quick_sort(arr, low, pi-1)
    quick_sort(arr, pi+1, high)

def quick_sort_helper(arr):
  quick_sort(arr, 0, len(arr)-1)
  return arr

arr = list(range(0, 80000))
# arr = [0]*5000
# random.shuffle(arr)
quick_sort_helper(arr)
print(recursion_cnt)