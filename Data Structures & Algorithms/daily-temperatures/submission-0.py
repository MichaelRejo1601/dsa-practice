class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [(temperatures[0],0)] #(temp, indx)

        for i in range(1, len(temperatures)):
            while True:
                if stack and stack[-1][0] < temperatures[i]:
                    res[stack[-1][1]] = i - stack[-1][1] #res[indx] = current_indx - indx
                    stack.pop()
                else:
                    break
            stack.append((temperatures[i], i))
        
        return res

            
        
            
