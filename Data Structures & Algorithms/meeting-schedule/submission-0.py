"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
"""
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts. The intervals may be provided in any order.

for for interval()
is there any conflicts?

0 space

O(n^2)

sort(start time)

nlogn

[][] 

interval.end interval+1.start
"""


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        last_end = -1
        for interval in intervals:
            if interval.start < last_end:
                return False
            last_end = interval.end

        return True

