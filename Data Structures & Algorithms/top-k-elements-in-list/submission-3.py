class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} #num -> frequency
        for num in nums: 
            freq[num] = freq.get(num, 0) + 1 

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, frequency in freq.items():
            buckets[frequency].append(num)
        
        result = []
        i = len(buckets) - 1 

        while len(result) < k:
            result += buckets[i]
            i -= 1  
        
        return result[:k]
        
