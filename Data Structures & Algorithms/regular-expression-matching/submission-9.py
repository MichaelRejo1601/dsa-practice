from functools import cache 

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def returnTrue_ifMatch(s_i, p_i):
            
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

