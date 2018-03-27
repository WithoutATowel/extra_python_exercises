# Given an array of integers, every element appears twice except for one.
# Implement a program that will print that single one.

# Example: [1,1,2,2,3,3,4,5,5,6,6,7,7] - 4 would be the odd man out

# Note:
# Your algorithm should have a linear runtime complexity.


# *** your code here ***

def single_one(arr):
    my_arr = arr.sort()

    while (arr[len(arr) - 1] == arr[len(arr) - 2]):
        arr.pop()
        arr.pop()

    print("The number is", arr[len(arr)-1])

single_one([1,1,2,2,3,3,4,5,5,6,6,7,7])
