# You are given an array of integers stones where stones[i] represents the weight of the ith stone.

# We want to run a simulation on the stones as follows:

# At each step we choose the two heaviest stones, with weight x and y and smash them togethers

# If x == y, both stones are destroyed

# If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

# #is the revers true? y into x
# Continue the simulation until there is no more than one stone remaining.

# Return the weight of the last remaining stone or return 0 if none remain.

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            heapq.heappush(stones, (-1)*abs(a-b))
        return stones[0] * -1
