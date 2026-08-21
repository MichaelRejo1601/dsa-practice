# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def findDeepest(root, n):

            take_left = n
            take_right = n

            if root.left:
                take_left = findDeepest(root.left, n+1)
            if root.right:
                take_right = findDeepest(root.right, n+1)
            
            return max(take_left, take_right)
        
        if root:
            return findDeepest(root, 1)
        else:
            return 0