
from collections import deque

class Codec:
    
    delimiter = chr(2222)
    offset = 1111
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        q = deque([root])
        value_flag = True
        while q and value_flag:
            value_flag = False
            for _ in range(len(q)):
                node = q.popleft()
                if node is not None:
                    res += chr(node.val + self.offset)
                    q.append(node.left)
                    q.append(node.right)

                    value_flag = True

                else:
                    res += self.delimiter
                    q.append(None)
                    q.append(None)

        return res    
        #123##45    
        # #
        # 1##
        # 1#3##45########
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # 0 ->1,2 #n*2+1, n*2+2 n-1//2
        # 1 ->3,4 n*2+1, n*2+2
        # 2 ->5,6
        # [1,None,3,None,None,4]
        nodeList = []

        if data == self.delimiter:
            return None
        else:
            nodeList.append(TreeNode(ord(data[0]) - self.offset,None,None))
        
        for i in range(1,len(data)):

            char = data[i]

            if char != self.delimiter:
                child = TreeNode(ord(char) - self.offset, None, None)
                nodeList.append(child)
                parent = nodeList[(i-1)//2]

                if i%2 == 1:
                    parent.left = child
                else:
                    parent.right = child

            else:
                nodeList.append(None)
        
        return nodeList[0]