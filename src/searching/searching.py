arr1 = [6, 5, 4, 9, 5, 3, 4, 2]
arr2 = []


def linear_search(arr, target):
    # Check index = to target
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found



# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here


    return -1  # not found








lin_search = linear_search(arr1, -5)
print(lin_search)
