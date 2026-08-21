class Solution:
    def search(self, nums: List[int], target: int) -> int:
        b = 0
        t = len(nums) - 1

        while b <= t:
            i = (b + t) // 2

            if nums[i] > target:
                t = i - 1
            elif nums[i] < target:
                b = i + 1
            else:
                return i

        return -1
