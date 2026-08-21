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
                if len(stack) == 0:
                    return False
                check_matching = stack.pop()
                if sym != symbols[check_matching]:
                    return False
        
        if len(stack) != 0:
            return False
        
        return True
        