# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur1=l1
        cur2=l2

        dummy=ListNode()
        cur=dummy
        tens=0
        while cur1 or cur2 or tens>0:
            cursum=tens
            if cur1:
                cursum+=cur1.val
                cur1=cur1.next
            if cur2:
                cursum+=cur2.val
                cur2=cur2.next
            tens=cursum//10
            ones=cursum%10
            newNode=ListNode(ones)
            cur.next=newNode
            cur=cur.next
            
            
        return dummy.next
