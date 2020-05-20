# # TO-DO: complete the helper function below to merge 2 sorted arrays
def merge_sorted_arrays(arrayA, arrayB):
  mergedArray = []
  idxOne = 0
  idxTwo = 0

  # keep looping until the end is reached for one of the arrays
  while idxOne < len(arrayA) and idxTwo < len(arrayB):
    if arrayA[idxOne] < arrayB[idxTwo]:
      # if there is smaller, add it from arrayA
      mergedArray.append(arrayA[idxOne])
      idxOne += 1
    elif arrayA[idxOne] >= arrayB[idxTwo]: # duplicates here
      # if there is a larger or equal, add it from arrayB
      mergedArray.append(arrayB[idxTwo])
      idxTwo += 1
  print(mergedArray)
  
  # add the remaining items from the longer list
  while idxOne < len(arrayA):
    mergedArray.append(arrayA[idxOne])
    idxOne += 1
  while idxTwo < len(arrayB):
    mergedArray.append(arrayB[idxTwo])
    idxTwo += 1

  return mergedArray

# TEST merge

arrA = [1, 2, 8, 9, 12, 19, 26, 30, 33, 37]
arrB = [10, 20, 24, 30, 31, 49, 59, 62, 63, 71]

print(merge_sorted_arrays(arrA, arrB))

def merge_sort(arr):
  if len(arr) > 1: # array of one item is sorted!
    left = merge_sort(arr[:len(arr) // 2]) # left half
    right = merge_sort(arr[len(arr) // 2:]) # right half
    arr = merge_sorted_arrays(left, right)
    print(arr)

  return arr

# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
  left = start
  right = mid + 1

  # [left -- mid -- right]
  # left_array_idxs = left -> mid
  # right_array_idxs = mid -> right

  # eg: 2 < 3 do nothing
  if arr[mid] <= arr[right]: 
    return
    
  # [left -- mid -- right]
  # left_array_idxs = left -> mid
  # right_array_idxs = mid -> right
  
  # until we meet in the middle
  while left <= mid and right <= end: 
    r_value = arr[right]
    l_value = arr[left]
    
    # if the value is smaller, go to the next one
    if l_value <= r_value:
      left += 1
    else: # we have it  
      tmp_idx = right

      # in-place move until left meets right
      while tmp_idx != left: 
        arr[tmp_idx] = arr[tmp_idx - 1]
        tmp_idx -= 1
        
      arr[left] = r_value

      # next iteration
      left += 1
      mid += 1
      right += 1
  
  return arr # optional: needed for tests to pass

def merge_sort_in_place(arr, left, right):
  if left < right: 
    mp = left + (right - left) // 2

    # easy peasy
    merge_sort_in_place(arr, left, mp) #left
    merge_sort_in_place(arr, mp + 1, right) #right

    merge_in_place(arr, left, mp, right)

  return arr



# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    print("NO WAY")

    return arr

import random
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr2 = []
arr3 = [2]
arr4 = [0, 1, 2, 3, 4, 5]
arr5 = random.sample(range(200), 50)

print(arr1)
merge_sort_in_place(arr1, 0, len(arr1)-1)
print(arr1)