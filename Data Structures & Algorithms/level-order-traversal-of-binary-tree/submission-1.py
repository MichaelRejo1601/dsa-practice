# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Given a binary tree root
# return the level order traversal of it as a nested list
# where each sublist contains the values of nodes at a particular level in the tree, 
# from left to right.

# None is not added

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        result = []

        while q:
            proxyList = []
            for _ in range(len(q)):
                node = q.popleft()   
                proxyList.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(proxyList)

        return result
