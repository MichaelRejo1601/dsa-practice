from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def returnTrue_ifMatch(s_i, p_i):

            if p_i == len(p):
                if s_i == len(s):
                    return True
                else: 
                    return False

            
            take_and_move_p = False
            take_and_stay_p = False
            skip_wild_and_move_p = False

            is_match = (
                s_i < len(s) and
                (p[p_i] == s[s_i] or p[p_i] == '.')
            )

            is_part_of_wildcard = (
                p_i + 1 < len(p) and p[p_i + 1] == '*'
            )

            if is_part_of_wildcard:
                skip_wild_and_move_p = returnTrue_ifMatch(s_i, p_i + 2)

            if is_match and is_part_of_wildcard:
                take_and_stay_p = returnTrue_ifMatch(s_i + 1, p_i)

            if is_match:
                take_and_move_p = returnTrue_ifMatch(s_i + 1, p_i + 1)

            return skip_wild_and_move_p or take_and_stay_p or take_and_move_p

        return returnTrue_ifMatch(0, 0)
