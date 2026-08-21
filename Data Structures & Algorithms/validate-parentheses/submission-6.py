class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        
        for bracket in s:
            if bracket not in key:
                stack.append(bracket)
            else:
                if stack and stack[-1] == key[bracket]:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        else: 
            return False