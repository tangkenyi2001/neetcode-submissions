# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # given the root of a binary tree, give the sum of any non empty path
        # whats the idea, idea is if the left subtree is negative, we dont add it. 
        # each node should store its left path sum +cur node and right path sum +cur node
        # and left+right path +cur node 
        dummy=TreeNode()
        stack=[[root,dummy]]
        queue=deque([root])
        cur=root
        hashset={dummy:[0,0,0]}
        #should store node:map to [left,right,total], so each time we move to that node, we add the cur
        while queue:
            #issue is that the original one is not being put in 
            cur=queue.popleft()
            hashset[cur]=[0,0,0] #left sum or right sum, total
            if cur.left:
                queue.append(cur.left)
                stack.append([cur.left,cur])
            if cur.right:
                queue.append(cur.right)
                stack.append([cur.right,cur])
        res=-1*math.inf
        while stack:
            currentnode,parentnode=stack.pop()
            res=max(hashset[currentnode][0]+currentnode.val,hashset[currentnode][1]+currentnode.val,hashset[currentnode][0]+hashset[currentnode][1]+currentnode.val,res)
            #if current node is parentnode.left
            if currentnode==parentnode.left:
                hashset[parentnode][0]=max(hashset[parentnode][0],hashset[currentnode][0]+currentnode.val,hashset[currentnode][1]+currentnode.val)
            else:
                hashset[parentnode][1]=max(hashset[parentnode][1],hashset[currentnode][0]+currentnode.val,hashset[currentnode][1]+currentnode.val)
        return res
