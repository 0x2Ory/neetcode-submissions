# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        
        
        res = []

        q = deque()
        q.append(root)
        while q: 
            lenq = len(q)
            for i in range(lenq):
                nodes = q.popleft()
                
                if nodes.left:
                    q.append(nodes.left)
                
                if nodes.right:
                    q.append(nodes.right)

                if  i == lenq-1:
                    res.append(nodes.val)
            
        return res