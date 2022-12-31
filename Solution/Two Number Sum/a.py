''' Solutions to two number sum DSA problem'''
# Array = [0,1,2,3,4,5,6]
# Target = 3
# output_value = [1,2]


def two_sum(array, target):
    """This is a O(n^2) time complexity but O(1) space complexity solution to the problem.
    This solution uses two loops to solve the problem"""
    for value in range(len(array)):
        for val in range(len(array)):
            iteration_sum = array[value] + array[val]
            if iteration_sum == target:
                return [value, val]
    return []


print(two_sum([0, 1, 2, 3, 4], 7))
