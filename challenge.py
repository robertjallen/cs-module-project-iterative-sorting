# ''Add up and print the sum of all of the minimum elements of each inner array:
arr1 = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

# The expected output is given by:

# 4 + -1 + 9 + -56 + 201 + 18 = 175
def sum(arr):
  sum = 0
  for i in arr:
    j = min(i)
    sum += j
    print("Smallest element is:", j) 
    print(sum)

sum(arr1)   