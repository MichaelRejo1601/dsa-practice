class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1]*len(nums)

        prefix = 1 
        for i in range(1, len(nums)):
            prefix *= nums[i-1]
            result[i] *= prefix
        
        suffix = 1 
        for i in reversed(range(0, len(nums)-1)):
            suffix *= nums[i+1]
            result[i] *= suffix
        
        return result
