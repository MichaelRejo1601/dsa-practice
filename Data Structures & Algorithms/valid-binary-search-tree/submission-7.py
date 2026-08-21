# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev_val = None


        while stack or root: 
            while root: 
                stack.append(root)
                root = root.left 
        
            root = stack.pop()

            if prev_val is not None and prev_val >= root.val:
                return False

            prev_val = root.val 

            root = root.right

        
        return True