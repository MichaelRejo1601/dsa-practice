# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# give the kth smallest element 
# in a binary search tree that is in order traversal 
# stack 

# #add nodes to stack
# #visiting means popping them off

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = None
        def dfs(root):
            nonlocal count
            nonlocal result
            
            if root == None:
                return
            
            dfs(root.left)

            count += 1 
            if count == k:
                result = root.val
            
            dfs(root.right)
            return

        dfs(root)
        return result


            


