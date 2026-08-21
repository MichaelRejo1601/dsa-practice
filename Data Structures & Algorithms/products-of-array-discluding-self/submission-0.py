class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    result[i] *= nums[j] 
        return result