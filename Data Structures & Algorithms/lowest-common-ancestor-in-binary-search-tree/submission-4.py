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
        print(p.val)
        print(q.val)
        print("=")
        while True:
            print(root.val)
            if root.val == p.val or root.val == q.val:
                print("equal return")
                return root
            if root.val >= p.val and root.val >= q.val:
                print("left taken, root greater")
                root = root.left
                continue
            if root.val <= p.val and root.val <= q.val:
                print("right taken, root less")
                root = root.right
                continue
            else:
                print("split found")
                return root
