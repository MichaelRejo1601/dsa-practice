# Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.

# By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.

# the kth distinct element 

#what happens if its a reapeated number

#iterate through list
# save highest numbers we see
#reversable to be the n-kth smallest item

#we could use a heap 

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        data = []
        for element in nums:
            heapq.heappush(data, element)
            while len(data) > k:
                heapq.heappop(data)
        return data[0]