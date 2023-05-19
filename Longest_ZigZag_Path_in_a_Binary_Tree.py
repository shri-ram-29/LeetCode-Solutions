class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0, 0]

            left_len, right_len = dfs(node.left), dfs(node.right)

            nonlocal max_len
            max_len = max(max_len, left_len[1], right_len[0])

            return [1 + left_len[1], 1 + right_len[0]] 

        max_len = 0
        dfs(root)
        return max_len
