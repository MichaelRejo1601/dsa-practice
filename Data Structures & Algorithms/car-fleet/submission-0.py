from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []
        cars = [[position[i], speed[i]] for i in range(len(position))]
        cars.sort(key=lambda x : (-x[0], -x[1])) #front to back

        for car in cars:
            
            time = (target-car[0])/car[1]

            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)

            
