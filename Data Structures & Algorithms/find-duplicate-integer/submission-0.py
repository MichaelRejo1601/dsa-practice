# You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.


# positive integers
# There is exactly one repeated integer in nums, and every other integer appears at most once.

# one will not appear at all

# we can do a binary search to find the upset if we sort

# o(n) and o(1) space indicates 

# multiple passes?

# number = n 


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = 0
        hare = 0

        while True:
            tortoise = nums[tortoise]
            hare = nums[hare]
            hare = nums[hare]
            if tortoise == hare:
                break

        turtle = 0

        while True:
            turtle = nums[turtle]
            tortoise = nums[tortoise]
            if turtle == tortoise:
                break

        return turtle

