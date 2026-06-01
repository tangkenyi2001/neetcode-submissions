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

        def mergeSort(lists: List[Optional[ListNode]]):
            if len(lists)==0:
                return None
            if len(lists)==1:
                return lists[0]
            numberoflists=len(lists)
            l=mergeSort(lists[:numberoflists//2])
            r=mergeSort(lists[numberoflists//2:])

            return mergeLists(l,r)
        return mergeSort(lists)


#time complexity = k(m) where k is number of lists and m is the length of each list
            

