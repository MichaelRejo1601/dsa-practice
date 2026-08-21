class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        symbols = {
            "(" : ")",
            "{" : "}",
            "[" : "]",
        }
        for sym in s:
            if sym in symbols:
                stack.append(sym)
            else: 
                if stack and sym == symbols[stack[-1]]:
                    stack.pop()
                else: 
                    return False
        
        if stack:
            return False
        
        return True
        