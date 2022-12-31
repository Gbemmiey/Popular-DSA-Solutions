''' Solutions to two number sum DSA problem'''
# Array = [0,1,2,3,4,5,6]
# Target = 3
# output_value = [1,2]


def two_sum(array, target):
    """This is a O(n) time complexity 
    but O(n) space complexity solution to the problem.
    This solution uses hashtables to solve the problem.
    It creates a hashtable using dictionary to hold previous values
    that are not complemented with any number in the array to obtain target.
    This solution is dependent on the mathematical relationship
    between the two numbers and the target value"""
    previous_values = {}
    for i, value in enumerate(array):
        x = target - value
        if x in array:
            if x not in previous_values:
                return [i, array.index(x)]
        # if (x in array) and (x != value) and (x not in previous_values):
        #     return [i, array.index(x)]
        previous_values.update({x: "True"})
    return []

print(two_sum([3,3], 6))
