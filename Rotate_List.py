from typing import Optional
class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Get the length of the linked list
        length = 1; newHead = head
        while newHead.next:
            length, newHead = length+1, newHead.next 
            
        #Calculate the number of rotations required 
        k = k % length
        if k == 0:
            return head
        
        #Move the pointer to the node before the new head after rotation
        cur = head
        for _ in range(length-k-1):
            cur = cur.next
            
        #rotate the linked list
        newHead.next = head
        head = cur.next 
        cur.next = None
        
        return head
        
        
        