# You are given an array nums of integers, which may contain duplicates. Return all possible subsets.


# may contain duplicates
# return all the possible subsets

# The solution must not contain duplicate subsets. You may return the solution in any order.




class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        nums.sort()

        def addSubsets(subset, i):
            nonlocal res

            if i >= len(nums):
                res.append(subset)
                return
            
            c = 1 
            while i+c < len(nums) and i+c > 0 and nums[i+c] == nums[i+c-1]:
                c += 1

            if i < len(nums):
                addSubsets(subset + [nums[i]], i+1)
            addSubsets(subset, i+c)
            
            return

        addSubsets([],0)

        return res