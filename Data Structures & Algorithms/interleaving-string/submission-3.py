"""

You are given three strings s1, s2, and s3. Return true if s3 is formed by interleaving s1 and s2 together or false otherwise.

Interleaving two strings s and t is done by dividing s and t into n and m substrings respectively, where the following conditions are met


|n - m| <= 1, i.e. the difference between the number of substrings of s and t is at most 1.

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm

Interleaving s and t is s1 + t1 + s2 + t2 + ... or t1 + s1 + t2 + s2 + ...


1  

s t s t s 
t s t s t
t s t ss 

substring are not gaurenteed to be the same amount
0 <= s1.length, s2.length <= 100

0 <= s3.length <= 200

s3

Input: s1 = "aaaa", s2 = "bbbb", s3 = "aabbbbaa"

Output: true

Input: s1 = "", s2 = "", s3 = ""

Output: true

Input: s1 = "abc", s2 = "xyz", s3 = "abxzcy"

Output: false

my thought here is that i want to iteratet rhoguhn s3

look at both of the strings

greedy

see which one matches the longest, then when it ends, see if i can continue on the other string

at the end, I want to check 

i will approach this with recursion

end when we hit the end of len(s3) or when i and j are both out of bounds
"""

from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
            return False
        if s1 == "" and s2 == "" and s3 == "":
            return True
        
        @cache
        def interleave(i, j, z):
            
            if z == len(s3):
                if i == len(s1) and j == len(s2):
                    return True
                else:
                    return False
            
            if i == len(s1) and j == len(s2):
                if z == len(s3):
                    return True
                else:
                    return False
            
            take_i = False
            take_j = False
            if i < len(s1):
                if s1[i] == s3[z]:
                    take_i = interleave(i+1, j, z+1)
            if j < len(s2):
                if s2[j] == s3[z]:
                    take_j = interleave(i, j+1, z+1)

            return any([take_i, take_j])
        
        return interleave(0,0,0)
        