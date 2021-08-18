# https://en.wikipedia.org/wiki/Maximum_subarray_problem
# Description:
# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence 
# in an array or list of integers:
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

def max_sequence(arr):
    max_sum = 0
    current_sum = 0

    for i in arr:
        current_sum = max(0, current_sum + i)
        max_sum = max(max_sum, current_sum)

    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(max_sequence(arr))



    
