# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# give nt 

# invert the binary tree and return its root 

# left beome right

# subtrees 

# preorer traversal

# swap
# left
# swap 
# left
# swap
# right swa

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def preorder(root):

            if root == None:
                return

            tmp = root.left
            root.left = root.right
            root.right = tmp
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return root