# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

# string s and int k

# we can choose up to k characters


# give a string S


# replace up to 2 character
# longest sequence of the same character

# hmap 
# store the longestfoundgap between two characters
# the gap that is 

# when we iterate through this list, we see letters
# we must go through it at least once to understand all the different letters and their locations

# 1) we find a perfect fit and theres the same letters on the side
# 2) we find a couple close together that have gaps that are perfectly fillable 
# 2) we can fill a couple gaps, but not fully the rest 
# 2) we can just try to see the max length we get by filling gaps, and just toss the remainder on top
# 3) create list for each of them of the gaps between

# 1 <= s.length <= 100,000: huge
# 0 <= k <= s.length


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k >= len(s)-1:
            return len(s)
        
        maxLength = k + 1
        
        counts = defaultdict(int) # letter : count
        i = 0
        j = 0
        counts[s[j]] += 1

        while j < len(s):
            
            maxCount = max(counts.values())
            fillables = (j - i + 1) - maxCount

            if fillables <= k:
                maxLength = max(maxLength, j - i + 1)
                j += 1
                if j == len(s):
                    break
                counts[s[j]] += 1
            else:
                counts[s[i]] -= 1
                i += 1

    
        return maxLength