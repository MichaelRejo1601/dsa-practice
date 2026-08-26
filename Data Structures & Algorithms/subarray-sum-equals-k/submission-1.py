class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = defaultdict(int)
        hmap[0] = 1
        count = 0
        runningSum = 0
        for num in nums:
            runningSum += num
            count += hmap[runningSum-k]
            hmap[runningSum] += 1
        return count
