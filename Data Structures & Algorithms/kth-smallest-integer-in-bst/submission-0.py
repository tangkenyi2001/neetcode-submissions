# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root.left and not root.right:
            return root.val
        maxheap=[-1*root.val]
        heapq.heapify(maxheap)
        #min heap by default
        #i can make it a max heap with max length
        #what if i just traverse the whole tree 
        cur=root
        queue=deque([cur])
        while queue:
            curNode=queue.popleft()
            if curNode.left:
                heapq.heappush(maxheap,-1*curNode.left.val)
                if len(maxheap)>k:
                    heapq.heappop(maxheap)
                queue.append(curNode.left)
            if curNode.right:
                heapq.heappush(maxheap,-1*curNode.right.val)
                if len(maxheap)>k:
                    heapq.heappop(maxheap)
                queue.append(curNode.right)
        return -1*heapq.heappop(maxheap)
        
            
