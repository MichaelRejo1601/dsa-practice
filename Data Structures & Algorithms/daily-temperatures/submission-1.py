class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #(temp, indx)

        for i in range(0, len(temperatures)):
            while True:
                if stack and stack[-1][0] < temperatures[i]:
                    res[stack[-1][1]] = i - stack[-1][1] #res[indx] = current_indx - indx
                    stack.pop()
                else:
                    break
            stack.append((temperatures[i], i))
        
        return res

            
        
            
