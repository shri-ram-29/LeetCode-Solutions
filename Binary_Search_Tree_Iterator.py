# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self.push_roots(root)

    def next(self) -> int:
        node = self.stack.pop()
        self.push_roots(node.right)
        return node.val

    def hasNext(self) -> bool:
        return bool(self.stack)

    def push_roots(self, root: TreeNode):
        while root:
            self.stack.append(root)
            root = root.left
