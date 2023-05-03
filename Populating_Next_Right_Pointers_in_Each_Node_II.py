from collections import deque
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        q = deque([root])
        while q:
            level_size = len(q)
            prev_node = None
            for i in range(level_size):
                curr_node = q.popleft()
                if prev_node:
                    prev_node.next = curr_node
                prev_node = curr_node
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
                    
            prev_node.next = None
        
        return root