class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        table = set(nums)
        

        highest_length = 0

        for num in nums:
            if (num-1) not in table:
                i = 0
                while num+i in table:
                    i += 1
            
                highest_length = max(i, highest_length)
        
        return highest_length
