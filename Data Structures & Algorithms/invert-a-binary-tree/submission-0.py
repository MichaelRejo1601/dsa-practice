# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def reverseSubtrees(root):
            if root.left:
                reverseSubtrees(root.left)
            if root.right:
                reverseSubtrees(root.right)
            swap = root.left
            root.left = root.right
            root.right = swap
        
        if root: 
            reverseSubtrees(root)
        
        return root