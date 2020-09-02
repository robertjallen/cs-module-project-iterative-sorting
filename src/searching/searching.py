


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
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = arr[middle]
        if guess == target:
            return middle

        if target > guess:
            low = middle + 1

        else:
            high = middle - 1



    return -1  # not found







# sorted_nums = sorted(nums)
# bin_search = binary_search(sorted_nums, my_target)

lin_search = linear_search(arr1, -5)
print(lin_search)
# print(bin_search)
