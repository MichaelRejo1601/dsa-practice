import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^a-zA-Z0-9]", "", s)
        s = s.lower()
        print(s)
        if len(s) % 2 == 0:
            return hash(s[:len(s)//2]) == hash(s[len(s)//2:][::-1])
        else:
            return hash(s[:len(s)//2+1]) == hash(s[len(s)//2:][::-1])
