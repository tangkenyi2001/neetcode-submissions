# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def identical(root1,root2):
            if not root1 and not root2:
                return True
            if root1 and root2 and root1.val==root2.val:
                return identical(root1.left,root2.left) and identical(root1.right,root2.right)
            else:
                return False
        if not root and not subRoot:
            return True
        if not root and subRoot:
            return False
        stack=[]
        stack.append(root)
        while stack:
            cur=stack.pop()
            if cur.val==subRoot.val:
                if identical(cur,subRoot):
                    return True
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return False
        