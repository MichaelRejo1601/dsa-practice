# Given an array nums of unique integers, return all possible subsets of nums.

# The solution set must not contain duplicate subsets. You may return the solution in any order.

# the solution must not have dupes, any order is okay 

# assuming both the insdie oan doutsdie

# since they are unique integers, we dont need to worry about dupes, we can calculate these programatically

# create a full set for everything
# for each number, remove itself from a particular set of them

# #no items is a subset

# take or skip

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def addSubsets(subset, i):
            nonlocal res
            if i == len(nums):
                res.append(subset)
                return
                
            addSubsets(subset + [nums[i]], i+1) #take
            addSubsets(subset, i+1) #skip

            return 

        addSubsets([], 0)
        return res