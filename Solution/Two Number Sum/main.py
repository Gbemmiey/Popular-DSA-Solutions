''' Solutions to two number sum DSA problem'''
# Array = [0,1,2,3,4,5,6]
# Target = 3
# output_value = [1,2]


def two_sum_a(array, target):
    """This is a O(n^2) time complexity but O(1) space complexity solution to the problem.
    This solution uses two loops to solve the problem"""
    for value in range(len(array)):
        for val in range(len(array)):
            iteration_sum = array[value] + array[val]
            if iteration_sum == target:
                return [value, val]
    return []


print(two_sum_a([0, 1, 2, 3, 4], 7))


def two_sum_b(array, target):
    """This is a O(n) time complexity 
    but O(n) space complexity solution to the problem
    This solution uses hashtables to solve the problem"""

    return []


def two_sum_c(array, target):
    """This is a O(nlog(n)) time complexity
    but O(1) space complexity solution to the problem
    This solution uses left and right indices to solve the problem"""
    array.sort()

    return []
