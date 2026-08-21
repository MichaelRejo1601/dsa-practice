class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0 
        r = len(heights)-1

        def calculate_area(l, r):
            return (r-l) * min(heights[r], heights[l])

        while l < r:
            max_area = max(max_area, calculate_area(l, r))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area