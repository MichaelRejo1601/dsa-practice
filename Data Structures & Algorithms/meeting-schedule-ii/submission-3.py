"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
we want to iterate through the sorted times

start time matters to determine if its in the bounds of something
when we start, we push an end time to something that we can check the min end time

1) iterate through my sorted list
2) push the end times to the heap
3) check if my start time is under the end time
4) increase my count 
5) the minheap top meeting is over? remove 1 from teh count

0                40
   5  10 
         15 20 


max() 

40 
1
check 40 needs to be popped (by checking 5)
push 10
10, 40
2
15, 10 is at top of heap
pop 10 
-1
2
20,40

"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        minheap = []
        count = 0
        minCount = 0
        for interval in intervals:
            while minheap and minheap[0] <= interval.start:
                heapq.heappop(minheap)
                count -= 1
            count += 1
            minCount = max(count, minCount)
            heapq.heappush(minheap, interval.end)
        return minCount

