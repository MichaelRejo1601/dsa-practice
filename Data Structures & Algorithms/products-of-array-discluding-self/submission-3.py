class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1]*len(nums)

        prefix_tally = 1
        for i in range(len(nums)):
            result[i] *= prefix_tally
            prefix_tally *= nums[i]


        suffix_tally = 1
        for i in reversed(range(0, len(nums))):
            result[i] *= suffix_tally
            suffix_tally *= nums[i]

        return result