# TO-DO: Implement a recursive implementation of binary search
# the function signature is where the message gets passed down from 
# delegator to the delegate
def binary_search(arr, target, start, left, right):
    left = 0
    right = len(arr) - 1
    
    # base case
    
    # or we searched the whole array, i.e when left > right
    if left > right:
        return -1
    # how do we move closer to a base case
    # we'll stop when we either find the target
    else: 
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid 
        
        elif arr[mid] < target:
           return binary_search(arr, target, mid + 1, right )
        else:
            
            return binary_search(arr, target, left, mid - 1)
            # rule out the right side

arr = [3, 4, 6, 16, 26, 28, 52, 55]
print(binary_search(arr, 52, 0, len(arr)-1))
    
    


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    # figure out whether the input array is sorted is ascending or descending order
    # keep a boolean to indicate the order of the array
    if arr[0] > arr[1]
        is_ascending = False
    else:
        is_ascending = True
    # if the input array is ascending, call 'binarysearch' 
    if is_ascending:
        return binary_search(arr, target, 0, len(arr)-1)
    else:
        return descending_binary_searcg(arr,target, 0, len(arr)-1)

