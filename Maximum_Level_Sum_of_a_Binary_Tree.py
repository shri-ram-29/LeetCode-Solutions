# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])  # Initialize the queue with the root and its level
        maxSum = root.val  # Initialize the maximum sum with the root value
        maxLevel = 1  # Initialize the maximum level with 1

        while queue:
            levelSum = 0
            levelSize = len(queue)

            for _ in range(levelSize):
                node, level = queue.popleft()
                levelSum += node.val

                if node.left:
                    queue.append((node.left, level + 1))

                if node.right:
                    queue.append((node.right, level + 1))

            if levelSum > maxSum:
                maxSum = levelSum
                maxLevel = level

        return maxLevel