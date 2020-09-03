# import random
# import time
# random_range = 10000000
# size = 15000000
# nums = random.sample(range(size), size)
# my_target = 45
# nums = [28, 97, 84, 63, 66, 29, 90, 68, 96, 89, 15, 67, 8, 83, 46, 58, 49, 45, 26, 13]
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
    """
    Returns true if target is in arr, else false
    """
    # remember to check the empty case
    # start = the starting index of the subset of the array we're searching in. inclusive
    # end = the end index of the subset -- inclusive
    start = 0
    end = len(arr) - 1
    while end >= start:
        # Look at the middle
        # how do we get the midpoint?
        # for the whole array, it's len(arr) / 2 - 1
        # for a subset of the array: (start + end) // 2
        middle_index = (start + end) // 2
        middle_value = arr[middle_index]
        # Compare it to the target
        if target == middle_value:
            return middle_index
        if target > middle_value:
            # search the right side
            # set start = middle_index + 1
            start = middle_index + 1
        if target < middle_value:
            # search the left side: set end = middle_index - 1
            end = middle_index - 1
        # Repeat
    # If not found, return False
    return -1
    # How do we know if it's not found?
        # the subset that we're looking at has 0 or negative length
    # How to represent the subset / "window" that we're searching in?
        # store start and end index in variables
        # start index + length of the subarray
        # pass around slices of the array - creates a new array, would use extra memory and time. you also lose the original indices
# sorted_nums = sorted(nums)
# bin_search = binary_search(sorted_nums, my_target)
lin_search = linear_search(arr1, -5)
print(lin_search)
# print(bin_search)