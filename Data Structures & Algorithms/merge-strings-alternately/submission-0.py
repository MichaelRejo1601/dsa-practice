# You are given two strings word1 and word2.

# Merge the strings by adding letters in alternating order

# which ne do we sar with 


# If a string is longer than the other, append the additional letters onto the end of the merged string.



class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        res = ""
        while i < len(word1) and i < len(word2):
            res += word1[i]
            res += word2[i]
            i += 1 
            
        res += word1[i:]
        res += word2[i:]

        return res

            