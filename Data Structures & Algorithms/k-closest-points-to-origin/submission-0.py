"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).


Given an array of points [x,y] and an integer k. 
return the k closest points to the origin

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

we must precompute the distance between the items - graphs?

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

closest points to the origin->

we can store them in a minheap for each coordinate, and then pop. 

1 <= k <= points.length <= 104

nlogn is not bad for 10000
-104 <= xi, yi <= 104

"""

import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(minheap, [distance, point])
        
        return [heapq.heappop(minheap)[1] for i in range(k)]