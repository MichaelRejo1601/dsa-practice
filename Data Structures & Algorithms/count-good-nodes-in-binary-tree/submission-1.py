# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# Within a binary tree, a node x is considered good if the path from the root of the tree to the node x contains no nodes with a value greater than the value of node x


# Given the root of a binary tree root, return the number of good nodes within the tree.

# 1 <= number of nodes in the tree <= 100,000 #large amount of nodes in tree

# -100 <= Node.val <= 100 #small value


# #We start from the root 
# #Do a DFS
# #Go down to the deeest node, saving highest number in a stack
# #root included in here
# #pop stack as we return
# #Check top of stack 
# #add to the stack everytime we traverse, adding the max value at each part
# # add to the good count
# #equal is good

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        stack = [float('-inf')]
        count = 0
        
        def dfs(root):
            nonlocal count

            if root == None:
                return
        
            if root.val >= stack[-1]:
                count += 1
                stack.append(root.val)
            else:
                stack.append(stack[-1])
            
            dfs(root.left)
            dfs(root.right)
            stack.pop()
            return

        dfs(root)

        return count
        