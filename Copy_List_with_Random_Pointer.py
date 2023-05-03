from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        p = head
        while p:
            n = Node(p.val, p.next)
            p.next = n
            p = p.next.next
        p = head
        while p:
            cloned_node = p.next
            if p.random:
                cloned_node.random = p.random.next
            else:
                cloned_node.random = None
            p = p.next.next
        old = head
        out = new = head.next
        while old:
            old.next = old.next.next
            if new.next:
                new.next = new.next.next
            else:
                new.next = None
            old = old.next
            new = new.next
        return out