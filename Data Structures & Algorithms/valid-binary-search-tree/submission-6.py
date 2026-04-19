# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(cur,minbound,maxbound) -> bool:
            #basecase if cur is none
            if cur is None:
                return True
            if cur.val>=maxbound or cur.val<=minbound:
                return False
            right=dfs(cur.right,cur.val,maxbound)
            left=dfs(cur.left,minbound,cur.val)

            return left and right
        minbound=-1*math.inf
        maxbound=math.inf
        return dfs(root,minbound,maxbound)

            
            