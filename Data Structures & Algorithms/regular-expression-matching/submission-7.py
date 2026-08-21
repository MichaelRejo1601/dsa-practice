# You are given an input string s consisting of lowercase english letters
# - string
# and a pattern p consisting of lowercase english letters, as well as '.', and '*' characters.
# - pattern (string+wild chars)
# Return true if the pattern matches the entire input string, otherwise return false.

# '.' Matches any single character
# - matches one characters

# '*' Matches zero or more of the preceding element.
# -matches any 

# s_i (position in s)
# p_i (position in p)

# take(if equal or wildcard)? 
# s_i + 1, p_i + 1? (if wildcard)

# skip (if wildcard)

# return True

# base case: 
# when p_i == len(p) and s_i == len(s):
# or when p_i == len(p):

# how do we compare 

# s == ., *, or s

# check if the nextcharacter is a 

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def returnTrue_ifMatch(s_i, p_i):
            
            print(s_i, p_i)
            if (p_i == len(p) or (p_i == len(p)-1 and p[p_i] == '*') or (p_i == len(p)-2 and p[p_i+1] == '*'))  and s_i == len(s):
                return True
            
            if p_i == len(p) or s_i == len(s):
                return False            

            take_and_move_p = False
            take_and_stay_p = False
            skip_wild_and_move_p = False

            is_match = p[p_i] == '.' or p[p_i] == s[s_i]
            is_part_of_wildcard = p_i < len(p)-1 and p[p_i+1] == '*'

            if is_match:
                take_and_move_p = returnTrue_ifMatch(s_i+1, p_i+1)
                if is_part_of_wildcard:
                    take_and_stay_p = returnTrue_ifMatch(s_i+1, p_i)
            
            if is_part_of_wildcard:
                skip_wild_and_move_p = returnTrue_ifMatch(s_i, p_i+2)

            return take_and_move_p or take_and_stay_p or skip_wild_and_move_p

        return returnTrue_ifMatch(0, 0)

