# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = None 
        def dfs(root):
            nonlocal count
            nonlocal res
            if root != None:

                left = dfs(root.left)
                if left == True:
                    return True
                
                
                count += 1
                if count == k: 
                    res = root.val
                    return True
                
                right = dfs(root.right)
                if right == True:
                    return True
                
                return False
            return False

        dfs(root)
        return res