# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeLists(list1,list2):
            cur1=list1
            cur2=list2
            dummy=ListNode(0)
            cur=dummy
            while cur1 and cur2:
                if cur1.val<cur2.val:
                    cur.next=cur1
                    cur1=cur1.next
                else:
                    cur.next=cur2
                    cur2=cur2.next
                cur=cur.next
            if cur1:
                cur.next=cur1
            elif cur2:
                cur.next=cur2
            return dummy.next
        #base cases
        if not lists:
            return None
        if len(lists)==1:
            return lists[0]
        cur=mergeLists(lists[0],lists[1])
        for i in range(2,len(lists)):
            cur=mergeLists(cur,lists[i])
        return cur
            
            

