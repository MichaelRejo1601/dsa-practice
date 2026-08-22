import heapq

class KthLargest:


    def __init__(self, k: int, nums: List[int]):
        self.data = []
        self.nth = k 
        for val in nums:
            heapq.heappush(self.data, val)
            while len(self.data) > self.nth:
                heapq.heappop(self.data)

    def add(self, val: int) -> int:
        heapq.heappush(self.data, val)
        while len(self.data) > self.nth:
            heapq.heappop(self.data)
        return self.data[0]
