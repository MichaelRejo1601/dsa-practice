# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.result = False
        def dfs(root):
            if root is None:
                return
            
            if root.val == subRoot.val:
                res = returnTrue_ifTreesEqual(root, subRoot)
                if res:
                    self.result = True
                
            dfs(root.left)
            dfs(root.right)
            
        def returnTrue_ifTreesEqual(r, s):
            if r is None or s is None:
                if r is None and s is None:
                    return True
                else:
                    return False
                
            if r.val == s.val:
                return returnTrue_ifTreesEqual(r.left, s.left) and returnTrue_ifTreesEqual(r.right, s.right)
                
            else:
                return False
        
        dfs(root)
        return self.result