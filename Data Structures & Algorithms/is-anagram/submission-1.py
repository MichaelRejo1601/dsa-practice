class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        zero_array = [0] * 26 
        for i in range(len(s)):
            zero_array[ord(s[i])-ord('a')] += 1 
            zero_array[ord(t[i])-ord('a')] -= 1 
        
        for num in zero_array:
            if num != 0:
                return False
        return True
        