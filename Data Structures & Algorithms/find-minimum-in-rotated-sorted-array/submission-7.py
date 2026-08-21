class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        l = 0 
        r = len(nums)-1
        
        while True:
            k = (l+r)//2 
            if nums[k] < nums[k-1]:
                return nums[k]
            
            elif nums[r] > nums[k]:
                r = k
            
            else:
                l = k+1
        
            


                                                              