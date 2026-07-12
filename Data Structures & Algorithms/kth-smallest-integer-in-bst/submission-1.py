# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #main idea of a bst is that parent node is always between the left node and right node
        #how do I find smallest value anyway, will be left most root
        # its kinda recursive the left sub tree is also a bst, right side as well
        stack=[]
        queue=[]
        # access the left followed by bottom 
        # in order trave
        cur=root
        # while there are still nodes,havent finished visiting
        # we keep going down the left node
        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            queue.append(cur.val)
            cur=cur.right
        return queue[k-1]
                

