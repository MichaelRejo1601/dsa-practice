"""
You are given two strings word1 and word2, each consisting of lowercase English letters.

You are allowed to perform three operations on word1 an unlimited number of times:

Insert a character at any position
Delete a character at any position
Replace a character at any position

Return the minimum number of operations to make word1 equal word2.

Example 1:

Return the minimum number of operations to make word1 equal word2.


Input: word1 = "neatcdee", word2 = "neetcode"

Output: 3

0 <= word1.length, word2.length <= 100

neatcdee

neatcdee -> neetcdee (replace a with e)
neetcdee -> neetcde (remove last e)
neetcde -> neetcode (insert o)

len(word1) > len(word2) - delete
len(word2) > len(word1) - insert
len(word2) == len(word1) - replace

O(n) 

keep track of their original positions
sort() a copy that is ziped with their indexes

sort()

sorted
original

neeeatdc
neeeatcdo


neetcode
codeneet
theres nothing wrong

so the position matters
we could store the positions into hmap, keep them updated as we make adjustments

swaping two is two replacements
inserting one is one 
deleting one is one
neetcode

coneetco
n operations is the maximum (replace/insert/delete everything)

insert in the middle reqires knowing that the rest of the string is in order and worth keeping
take or skip, for each we could either replace or delete

1) inserting means we have less len otherwise its never worth it 
2) deleting means we have more len otherwise its never worth it

replace, replace, replace, replace, insert, repla

"""
from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @cache
        def minOperations_toReachEnd(str1, str2):

            delete = float('inf')
            replace = float('inf')
            insert = float('inf')
            skip = float('inf')

            if len(str1) == 0 and len(str2) == 0:
                return 0
            if len(str1) == 0:
                return 1 + minOperations_toReachEnd(str2[0] + str1, str2)
            if len(str2) == 0: 
                return 1 + minOperations_toReachEnd(str1[1:], str2)
            
            if str1[0] != str2[0]:
                if len(str1) > 0:
                    delete = 1 + minOperations_toReachEnd(str1[1:], str2)
                    if len(str2) > 0:
                        replace = 1 + minOperations_toReachEnd(str1[1:], str2[1:])
                insert = 1 + minOperations_toReachEnd(str2[0] + str1, str2)

            else:
                skip = minOperations_toReachEnd(str1[1:], str2[1:])
                
            return min(min(skip, delete), min(replace, insert))

        
        return min(max(len(word1), len(word2)), minOperations_toReachEnd(word1, word2))
