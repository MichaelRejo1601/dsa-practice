# You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

# You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.


# Return the minimum integer k such that you can eat all the bananas within h hours.

# decide a bananas per hour reating rate

# from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles.sort()

        min = 1
        max = piles[-1]

        def isKValid(k):
            hrs_taken = 0
            i = 0
            while hrs_taken < h and i < len(piles):
                hrs_taken += piles[i] // k 
                remainder = piles[i] % k
                if remainder > 0:
                    hrs_taken += 1
                i += 1

            return i >= len(piles) and hrs_taken <= h


        while min < max:
            k = (min+max)//2

            if isKValid(k):
                max = k
            else:
                min = k + 1

        return min