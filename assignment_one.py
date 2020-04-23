import collections
import heapq


'''
Given an array a of n numbers and a target value t, find two numbers whose sum is t.
Example: a=[5, 3, 6, 8, 2, 4, 7], t=10  ⇒  [3, 7] or [6, 4] or [8, 2]
Clarifying Qs:
- Can the target be 0? If so, does that require finding two zeros?
- Can the list be empty and have a valued target?
- Should I return a list or a tuple?
- Am I able to return an empty list/tuple if no two numbers are found?
'''

def solution_one(arr: list, target: int) -> tuple:
    '''
    O(1 + n + n) -> O(n)
    '''
    # O(1) - Checking if array is truthy and has a len higher than 1.
    if not arr or len(arr) < 1:
        return []

    # O(n) - Converting all elements of a list into a set.
    arr_as_set = set(arr)

    # O(n) - Iterating over numbers in the array.
    for num in arr:
        needed_num = target - num

        # O(1) - Checking if the number is in a set. (Mostly const)
        if needed_num in arr_as_set:
            return (num, needed_num)

    return []

def solution_two(arr: list, target: int) -> tuple:
    '''
    O(1 + n + 1) -> O(n)
    '''
    # O(1) - Checking if array is truthy and has a len higher than 1.
    if not arr or len(arr) < 1:
        return None

    seen = {}
    # O(n)
    for i, value in enumerate(arr):
        # O(1)
        if value in seen:
            return (arr[seen[value]], arr[i])
        seen[(target - value)] = i
    return []

print(solution_one([5, 3, 6, 8, 2, 4, 7], 10))
print(solution_two([5, 3, 6, 8, 2, 4, 7], 10))

'''
Given an array a of n numbers and a count k find the k largest values in the array a.
Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  ⇒  [6, 8, 7]

Simplifications:
-
'''
def solution_one(array, k):
    # O(nLogn)
    return sorted(array, reverse=True)[:k]

def solution_two(array, k):
    # O(nLogn)
    return heapq.nlargest(k, array)


print(solution_one([5, 1, 3, 6, 8, 2, 4, 7], 3))
print(solution_two([5, 1, 3, 6, 8, 2, 4, 7], 3))

'''
Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  t=20  ⇒  [13, 6] or [4, 17] or [5, 14]

simplifications:
- Assume the arrays are of equal length.
- You can always make t out of the arrays.
'''

def solution_one(first_array, second_array, target):
    # Initialize the diff between  
    # pair sum and x. 
    first_arr_sorted = sorted(first_array)
    second_arr_sorted = sorted(second_array)
    diff=float("inf")

    solutions = []
    left_index = 0
    right_index = len(second_arr_sorted) - 1

    # While we haven't gone out of bounds, keep obtaining differences.
    while(left_index < len(first_arr_sorted) and right_index >= 0):
        # If the new diff is less than the old diff, reset solutions. If it is equal, add them!
        if abs(first_arr_sorted[left_index] + second_arr_sorted[right_index] - target) < diff:
            diff = abs(first_arr_sorted[left_index] + second_arr_sorted[right_index] - target)
            solutions = [(first_arr_sorted[left_index], second_arr_sorted[right_index])]
        elif abs(first_arr_sorted[left_index] + second_arr_sorted[right_index] - target) == diff:
            solutions.append((first_arr_sorted[left_index], second_arr_sorted[right_index]))

        # Move indices based on if our sum is greater or less than the target value.
        if first_arr_sorted[left_index] + second_arr_sorted[right_index] > target:
            right_index=right_index-1
        else:
            left_index=left_index+1

    return solutions

print(solution_one([9, 13, 1, 8, 12, 4, 0, 5], [3, 17, 4, 14, 6], 20))
# Couldn't really come up with a solution 2 that was more optimal/didn't cover the edge cases covered here
