# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        stack = [root.val] 
        count = 0 

        def dfs(node):
            nonlocal count
            
            if node == None:
                return

            if node.val >= stack[-1]:
                stack.append(node.val)
                count += 1
            
            else:
                stack.append(stack[-1])
            
            dfs(node.right)
            dfs(node.left)

            stack.pop()

        dfs(root)
        return count