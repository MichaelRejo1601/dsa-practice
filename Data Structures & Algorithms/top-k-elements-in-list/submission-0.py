class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} #num -> frequency
        for num in nums: 

            freq[num] = freq.get(num, 0) + 1 

        freq_list = []
        for num in freq: 
            freq_list.append((freq[num], num))
        
        print(freq_list)
        result = [num for (freq, num) in sorted(freq_list, reverse=True)[:k]]                                              
        return result