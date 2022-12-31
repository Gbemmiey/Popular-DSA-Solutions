''' Solutions to two number sum DSA problem'''
# Array = [0,1,2,3,4,5,6]
# Target = 3
# output_value = [1,2]


def two_sum(array, target):
    """This is a O(n^2) time complexity but O(1) space complexity solution to the problem.
    This solution iterates twice over the input space to solve the problem.
    The function returns an empty array if there is no solution"""
    for i, value in enumerate(array):
        for j, val in enumerate(array[i+1 : len(array)]):
            iteration_sum = value + val
            if iteration_sum == target:
                return [i, j+i+1]

    return []

# This solution used enumerate(array) instead of range(len(array)
# in the for loop.

# for value, i in enumerate(array):
# for value in range(len(array)):

# When using enumerate with a for loop, You use two variables to control the loop
# The first variable declared would be the index
# while the second variable is the value

# In the above function: i = array[value]
# and j = array[val]
