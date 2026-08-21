class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        # if len(s) != len(t):
        #     return False
        
        # hash_count = 0

        # for i in range(len(s)):

        #     hash_count += hash(s[i])
        #     hash_count -= hash(t[i])


        # if hash_count == 0:
        #     return True
        
        # return False    