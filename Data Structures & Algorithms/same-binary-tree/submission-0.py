# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        self.result = True

        def dfs_2(root1, root2):

            if root1 and root2 and root1.val != root2.val:
                self.result = False

            if root1 is None or root2 is None:
                if root1 != root2:
                    self.result = False
                return True
            
            left = dfs_2(root1.left, root2.left)
            right = dfs_2(root1.right, root2.right)



            return left and right


        dfs_2(p, q)
        return self.result