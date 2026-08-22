# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# get P and Qs values
# check root 
# where does it split, tht is the lowest common ancestor. 
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while True:
            if root.val > p.val and root.val > q.val:
                root = root.left
                continue
            if root.val < p.val and root.val < q.val:
                root = root.right
                continue
            else:
                return root
