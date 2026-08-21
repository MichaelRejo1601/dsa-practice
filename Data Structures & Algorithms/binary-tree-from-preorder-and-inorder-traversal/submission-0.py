
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]: 

        self.i = 0
        inorder_map = {x:i for i,x in enumerate(inorder)}
        
        def dfs(l, r):
            
            if l > r:
                return None
            
            current_num = preorder[self.i]
            self.i += 1 

            root = TreeNode(current_num, None, None)

            m = inorder_map[current_num]
            
            root.left = dfs(l, m-1)

            root.right = dfs(m+1, r)
            
            return root

        return dfs(0, len(preorder)-1)
