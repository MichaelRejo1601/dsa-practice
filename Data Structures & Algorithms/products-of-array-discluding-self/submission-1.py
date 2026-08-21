class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]*len(nums)
        suffix = [nums[-1]]*len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        for i in reversed(range(0, len(nums)-1)):
            suffix[i] = suffix[i+1] * nums[i]

        result = []
        
        result.append(suffix[1])
        for i in range(1,len(nums)-1):
            result.append(prefix[i-1]*suffix[i+1])
        result.append(prefix[-2])

        print(prefix)
        print(suffix)
        return result