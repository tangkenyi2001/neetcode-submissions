# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        temp=head
        length=0
        while temp:
            length+=1
            temp=temp.next
        nfromfront=length-n
        cur=head
        if nfromfront==0:
            temp=cur.next
            cur.next=None
            return temp
        for _ in range(nfromfront-1):#move to infront of deleted node
            cur=cur.next
        post=cur.next.next
        cur.next=post
        return head
