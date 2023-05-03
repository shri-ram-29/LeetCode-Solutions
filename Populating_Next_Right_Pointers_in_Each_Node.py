class Node:
    def __init__(self, val:int = 0,left: 'Node'=None, right:'Node'=None, next: 'Node'=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
from collections import deque, Optional
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.dfs(root)
        return root
    def dfs(self,root):
        if root == None or root.left == None:
            return
        root.left.next = root.right
        if root.next !=None:
            root.right.next = root.next.left
        self.dfs(root.left)
        self.dfs(root.right)