# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.max_path = 0

        def dfs(root): # -> return [max_path_found, max_depth]
            
            if root == None:
                return -1
                        
            left_max_depth = dfs(root.left) + 1
            right_max_depth = dfs(root.right) + 1

            path = left_max_depth + right_max_depth

            self.max_path = max(path, self.max_path)

            return max(left_max_depth, right_max_depth)
        
        dfs(root)

        return self.max_path