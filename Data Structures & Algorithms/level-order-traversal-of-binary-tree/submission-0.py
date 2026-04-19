# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=[]
        q.append(root)
        length=0
        res=[]
        curarr=[]
        while q:
            if length==0:
                length=len(q)
            cur=q.pop(0)
            curarr.append(cur.val)
            if len(curarr)==length:
                res.append(curarr)
                curarr=[]
                length=0
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return res