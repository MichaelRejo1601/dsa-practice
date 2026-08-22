# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
# #         self.right = right
# The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.

# the path can be through the root at a T bone

# The length of a path between two nodes in a binary tree is the number of edges between the nodes. Note that the path can not include the same node twice.


# number of edges

# Given the root of a binary tree root, return the diameter of the tree.
# 2 longest limbs
# return the length of the limb


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxElbowTracker = 0

        def returnLength_ofLongestLimb_startingFrom(root):
            nonlocal maxElbowTracker

            left = 0
            right = 0
            if root.left:
                left = 1+returnLength_ofLongestLimb_startingFrom(root.left)
            if root.right:
                right = 1+returnLength_ofLongestLimb_startingFrom(root.right)
            

            maxElbowTracker = max(maxElbowTracker, left+right)
            return max(left,right) #returning longest limb of the two

        returnLength_ofLongestLimb_startingFrom(root)
        return maxElbowTracker

