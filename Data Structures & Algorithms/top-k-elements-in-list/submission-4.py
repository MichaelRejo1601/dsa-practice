class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        freq_list = []
        for num, frequency in freq.items():
            freq_list.append((frequency, num))
        
        return [j for i, j in sorted(freq_list, reverse=True)[:k]]
