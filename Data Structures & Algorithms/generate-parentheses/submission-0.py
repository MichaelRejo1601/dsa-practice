class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(chain: str, openers_left: int, closers_left: int, result: list):

            if closers_left == 0:
                result.append(chain)
                return
            
            if closers_left > openers_left:
                dfs(chain+")", openers_left, closers_left-1, result)
            
            if openers_left:
                dfs(chain+"(", openers_left-1, closers_left, result) 

        dfs("", n, n, result)

        return result