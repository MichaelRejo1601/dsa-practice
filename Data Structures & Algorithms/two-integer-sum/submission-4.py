# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.


# return the indeices, they cannot be the same
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# return smaller one first

# how can we get the target sum 

# is the array sorted?
 # no the array is not sorted
# no dupes
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i in range(len(nums)):
            mem[nums[i]] = i
        
        for i in range(len(nums)):
            check = mem.get(target-nums[i], -1)
            if check != -1 and check != i:
                return [i, check]