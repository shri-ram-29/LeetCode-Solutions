# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            nonlocal minDiff, prev 
            if not node:
                return
            inorder(node.left)
            if prev is not None:
                minDiff = min(minDiff, node.val - prev)
            prev = node.val
            inorder(node.right)
        
        minDiff = float('inf')
        prev = None
        inorder(root)
        return minDiff
