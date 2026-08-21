class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1 

        while l <= r: 
            #split middle
            i = (l+r)//2 

            if nums[i] == target: 
                return i
            
            #if left side is sorted
            if nums[l] <= nums[i]:
                # if in that half
                if nums[l] <= target < nums[i]:
                    r = i - 1
                # else use the other half
                else:
                    l = i + 1
            # else right side is sorted
            else:
                # if in that half
                if nums[i] < target <= nums[r]:
                    l = i + 1
                # else use other half
                else:
                    r = i - 1

        return -1
