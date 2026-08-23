# You are given a string digits made up of digits from 2 through 9 inclusive.

# Each digit (not including 1) is mapped to a set of characters as shown below:

# A digit could represent any one of the characters it maps to.

# Return all possible letter combinations that digits could represent. You may return the answer in any order.

# #each of these are in 3, so we can just do that





class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneMap = {
            "2":['a', 'b', 'c'],
            "3":['d', 'e', 'f'],
            "4":['g', 'h', 'i'],
            "5":['j', 'k', 'l'],
            "6":['m', 'n', 'o'],
            "7":['p', 'q', 'r', 's'],
            "8":['t', 'u', 'v'],
            "9":['w', 'x', 'y', 'z']
        }

        result = []
        def addCombination(word, i):
            if i >= len(digits):
                result.append(word)
                return 
            
            for letter in phoneMap[digits[i]]:
                addCombination(word + letter, i + 1)

            return
        
        addCombination("", 0)
        return result if result != [""] else []
