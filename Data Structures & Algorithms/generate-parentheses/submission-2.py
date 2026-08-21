class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        results = []
        def addParentheses_toString_opensLeft_closesLeft_addToList(res:str, opens: int, closes: int):
            if closes == 0: 
                results.append(res)
            if opens < closes:
                addParentheses_toString_opensLeft_closesLeft_addToList(res + ")", opens, closes - 1)
            if opens:
                addParentheses_toString_opensLeft_closesLeft_addToList(res + "(", opens - 1, closes)
        
        addParentheses_toString_opensLeft_closesLeft_addToList("", n, n)
        return results