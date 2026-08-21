class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = set()
        for num in nums:
            table.add(num)

        highest_length = 0

        for num in nums:
            i = 0
            while num+i in table:
                i += 1
            if i > highest_length:
                highest_length = i
        
        return highest_length
