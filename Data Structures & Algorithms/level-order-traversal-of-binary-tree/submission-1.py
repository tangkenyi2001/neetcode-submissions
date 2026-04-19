# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        res=[]
        queue=[]
        queue.append(root)
        while queue:
            size=len(queue)
            arr=[]
            for i in range(size):
                cur=queue.pop(0)
                arr.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(arr)
        return res