# given two strings text1 and text2
# -given two strings
# -have no relation to one another 

# return the legnth of the longest common subsequence between the two strings 
# -they are a sequence
#     - the order must be retained 
# - returns a number

# if one exists 
# - return 0 if none

# A subsequence is a sequence
# - ordered

# that can be derived from the given sequence by deleting some or no elements 
# - elements can be deleted from any spot
# - no deletions also counts as a subsequence
# - take (away) or skip
# - for each in the string

# without changing the relative order of the remaining characters
# - can be achieved by simply taking and skipping
# - how do I efficiently remove from/compare the two strings?

# actions: 
# given i (position in string1):
# take: del string[i], i remains same (next is moved into i)
# skip: string remains same, i + 1

# given j (position in string2):
# take del string2[i], i remains the same
# skip: string2 remains same, j + 1

# lols_sw_df_sw2_df2(string1, i, string2, j):
# ex. "cat" is a subsequence of "crabt"

# constaints:
# 1 <= length1, lenght2 <= 1000
# text1 and text2 only lowercase english characters

# basecase:
# - end of string
#  - i == len(string1)
#  - j == len(String2)
# - subsequence is found
#   - can take first since longest is needed.

# ret: max(4 actions)



from functools import cache

class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @cache
        def maxSubstring_startingFrom(i,j):
            if i == len(text1) or j == len(text2):
                return 0 
            if text1[i] == text2[j]:
                return 1 + maxSubstring_startingFrom(i+1, j+1)
            
            return max(maxSubstring_startingFrom(i+1,j), maxSubstring_startingFrom(i,j+1))

        return maxSubstring_startingFrom(0,0)

