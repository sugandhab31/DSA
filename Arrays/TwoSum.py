"""
Problem Statement
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may not use the same element twice.
You can return the answer in any order.
Assume that there is exactly one solution.
Example 1
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1] (since nums[0] + nums[1] = 2 + 7 = 9)

Example 2
Input: nums = [3, 2, 4], target = 6
Output: [1, 2] (since nums[1] + nums[2] = 2 + 4 = 6)

How do you approach this?
Think about:

Brute force approach (checking all pairs) – Time Complexity?
Using HashMap (Dictionary in Python) – How can we optimize it?
"""

def twoSum(arr, target):

    num_map = {}
    for i,num in enumerate(arr):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []
    
arr = [2, 7, 11, 15]
target = 9

print(twoSum(arr, target))