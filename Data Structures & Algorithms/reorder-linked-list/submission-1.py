# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        #traverse to middle
        mid=head
        r=head.next
        while r and r.next:
            r=r.next.next
            mid=mid.next
        #reverse middle to end
        prev=None
        cur=mid.next
        mid.next=None
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        #alternate left and right
        l=head
        r=prev
        while l and r:
            templ=l.next
            tempr=r.next
            l.next=r
            l=templ
            r.next=l
            r=tempr
        
        