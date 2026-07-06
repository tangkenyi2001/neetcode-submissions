# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur=root
        if p.val>q.val:
            higher=p
            lower=q
        else:
            higher=q
            lower=p
        
        while cur:
            if lower.val<=cur.val<=higher.val:
                return cur
            elif cur.val>higher.val and cur.val>lower.val:
                cur=cur.left
            else:
                cur=cur.right
        