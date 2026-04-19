# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #only return right sides
        #bfs last in queue
        if not root:
            return []
        q=[]
        q.append(root)
        length=0
        res=[]
        while q:
            length=len(q)
            temp=[]
            for _ in range(length):
                cur=q.pop(0)
                temp.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(temp[-1])
        return res
        
        
            


                
            