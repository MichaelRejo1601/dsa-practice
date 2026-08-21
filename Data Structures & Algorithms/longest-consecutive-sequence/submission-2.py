class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = set(nums)
        
        highest_length = 0

        for n in nums: 
            score = 1
            while n-1 in mp:
                score +=1 
                n -=1 

            highest_length = max(score, highest_length)
            
        return highest_length
            


