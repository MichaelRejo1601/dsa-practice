# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
 
#   5
#   37
#  14 68

#  iterate down to bottom left
#  when you hit the bottom, start returning until the 1th one

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = None

        def dfs(node):
            nonlocal count, result
            if not node or result is not None:
                return

            dfs(node.left)

            count += 1
            if count == k:
                result = node.val
                return

            dfs(node.right)

        dfs(root)
        return result