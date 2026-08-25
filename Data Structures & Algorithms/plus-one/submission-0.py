"""
You are given an integer array digits, where each digits[i] is the ith digit of a large integer. It is ordered from most significant to least significant digit, and it will not contain any leading zero.

Return the digits of the given integer after incrementing it by one.

"""

"""
each int is a base 10 digit
in order
no leading 0s

return the array back after incrementing by one
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        i = len(digits)-1
        while i > 0 and digits[i] == 10:
            digits[i] = 0
            digits[i-1] += 1
            i -= 1
        
        if digits[0] == 10:
            digits[0] = 0
            return [1] + digits
        return digits
        