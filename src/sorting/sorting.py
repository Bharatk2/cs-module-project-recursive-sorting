# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    
    # Your code here
    a = 0
    b = 0
    
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1
    
    # at this point, we've merged in all the elements from 
    # one of the arrays, but not the other
    
    # check both arrays to see if the poiunter is still in range
    
    if a < len(arrA):
        # arrA still has leftover elements
        # push them all the merged arrya
        merged_arr.exten(arrA[a:])
    if b < len(arrB):
        merged_arr.extend(arrB[b:])
    
    return merged_arr

arrA = [3, 6, 8, 12, 15]
arrB = [1, 4, 5, 9, 11]

print(merge(arrA, arrB))
# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # base case: stop splitting the arrays in half when the arrays
    # reach a length of 1
    if len(arr) > 1:
    # otherwise, keep splitting them in half
        # take the array from 0 and divided by two
        left = merge_sort(arr[0 : len(arr) // 2])
        right = merge_sort(arr[0 : len(arr) // 2 : ])
        arr = merge(left, right)
        

    return arr

arr = [45, 12, 89, 14, 67, 45, 23, 90, 11]
print(merge_sort(arr))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here

