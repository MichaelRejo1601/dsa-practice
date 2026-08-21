# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

# The path sum of a path is the sum of the nodes values in the path.

# create a graph

# find the maximum sum?

# what about calculating partial sums for every possible traversal down the path

# prefix sums?

# every node can be named by a series of movements from the root

# every maxPath down a given line can be determined by the root and the direction

# L:0, R:0, D:'R' (R)
# R:0, R:0, D:'L' (L)

# L:0, R:0

# cache the nodes like above

# we can calculate the maximumSumPath at a given node by calculating the leftleg (cahce) rightleg (cache) and root.val 

# we can record the maxmimumSumPath


# bottom up -> calculate maxPaths. How do we ignore the leaf node being a negative number? We could return three different choices

# TakeLeft, TakeRight, TakeNone

# return the Max of these

from functools import cache

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxVal = float("-inf")
        nodeMap = {}
        def populateMap(root, path):
            nonlocal nodeMap 
            if root is None:
                return
            nodeMap[path] = [root, root.val] #prepopulate with the bareminimum value for that side of the tree
            populateMap(root.left, path+"L")
            populateMap(root.right, path+"R")
        
        populateMap(root, "")
        # print(nodeMap)
        # DFS down to the bottom node. 
        # options are TakeLeft, TakeRight, TakeNone
        # TakeLeft = dfs(root.left, path)
        @cache
        def returnMaxPath_ifGoingDown(path):

            nonlocal maxVal

            if path not in nodeMap:
                return float("-inf")
            
            this = nodeMap[path][1]
            takeThis = this
            takeThisLeft = this + returnMaxPath_ifGoingDown(path + "L")
            takeThisRight = this + returnMaxPath_ifGoingDown(path + "R")
            takeLeft = returnMaxPath_ifGoingDown(path + "L")
            takeRight = returnMaxPath_ifGoingDown(path + "R")
            
            elbow = max(max(max(takeLeft + takeRight + takeThis, takeRight + takeThis), takeLeft + takeThis), takeThis)

            maxVal = max(elbow, maxVal)
            print(maxVal,  "#" + path, this)
            
            return max(max(takeThisLeft, takeThisRight), takeThis)

        returnMaxPath_ifGoingDown("")

        return maxVal

















