# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(val=0,next=head)
        fast,slow = dummy,dummy
        for _ in range(n):
            fast=fast.next
        while fast and fast.next:
            fast=fast.next
            slow=slow.next
        #now our fast slow node is in front of the node we want to remove
        temp=slow.next.next
        slow.next=temp
        return dummy.next
        
        
