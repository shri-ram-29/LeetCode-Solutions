class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.head = None
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while head:
            res = (res<<1)+head.val
            head = head.next
        return res