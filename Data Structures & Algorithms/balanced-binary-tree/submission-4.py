# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True

        self.result = True 

        def dfs(root):
            
            if root is None:
                return 0

            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right)

            if abs(left - right) > 1:
                self.result = False

            return max(left,right)

        dfs(root)

        return self.result