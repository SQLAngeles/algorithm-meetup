# QUICK SORT
import sys
import random

sys.setrecursionlimit(10000)
global recursion_cnt
recursion_cnt=0

def partition(arr,low,high):
  lt = low-1
  gt = high+1
  pivot = arr[high]

  for j in range(low , high):
    if arr[j] < pivot:
      lt += 1
      arr[lt], arr[j] = arr[j], arr[lt]
    elif arr[j] > pivot:
      gt -= 1
      arr[gt], arr[j] = arr[j], arr[gt]
  return lt+1, gt-1


def quick_sort(arr,low,high):
  global recursion_cnt
  if low < high:
    recursion_cnt += 1
    lt, gt = partition(arr,low,high)
    quick_sort(arr, low, lt-1)
    quick_sort(arr, gt+1, high)

def quick_sort_helper(arr):
  quick_sort(arr, 0, len(arr)-1)
  return arr

arr = [2]*2 + [1]*2 + [3]*2 + [10]*2 + [8]*2
quick_sort_helper(arr)
print(arr)
print(recursion_cnt)