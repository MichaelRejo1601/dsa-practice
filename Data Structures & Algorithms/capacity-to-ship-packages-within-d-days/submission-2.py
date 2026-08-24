# can we precomupute?
# weights = [2,4,6,1,3,10], days = 4


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxc = sum(weights)
        minc = max(weights)

        def checkValidCapacity(cap):
            current_days = 1
            current_capacity = 0

            for weight in weights:
                if current_capacity + weight <= cap:
                    current_capacity += weight
                else:
                    current_days += 1
                    current_capacity = weight

            return current_days <= days

        while minc < maxc:
            cap = (minc + maxc) // 2

            if checkValidCapacity(cap):
                maxc = cap
            else:
                minc = cap + 1

        return minc

