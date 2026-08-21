# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# we need some way to store the in order parents of each of the nodes
# then compare these two lists to see which is the first common parent. 

# BST -> higher values are on the right, lesser values on the left. 

# given 5 as the root 
# we know 3 must be on the left
# must be on the right
# therefore. 5 is the greatest ancestor. 

# We realize this when the options either split onto both sides of the tree, or when the number itself is found 

# BFS -> compare p and q to the left and right

# traverse down the path that you find it down

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        self.l = min(p.val, q.val)
        self.r = max(p.val, q.val)
        
        def dfs(root):
            if root.val == self.l or root.val == self.r:
                return root
            
            if root.val > self.l and root.val < self.r:
                return root 

            if root.val < self.l: 
                return dfs(root.right)

            if root.val > self.r:
                return dfs(root.left)

        return dfs(root)