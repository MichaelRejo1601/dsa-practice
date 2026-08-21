class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1 
        
        for num, frequency in freq.items():
            freq_buckets[frequency].append(num)
        
        result = []
        i = len(freq_buckets) - 1
        while len(result) < k:
            result += freq_buckets[i]
            i -= 1 
        return result[:k]