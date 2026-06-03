# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append([p,q])

        while queue:
            nodep, nodeq = queue.popleft()
            
            if nodep is None and nodeq is None:
                continue
            if nodep is None or nodeq is None or nodep.val != nodeq.val:
                return False

            queue.append((nodep.left, nodeq.left))
            queue.append((nodep.right, nodeq.right))

        return True




