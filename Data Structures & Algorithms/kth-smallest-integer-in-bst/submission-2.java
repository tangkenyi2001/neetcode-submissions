/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int kthSmallest(TreeNode root, int k) {
        //dfs
        Deque<TreeNode>stack=new ArrayDeque<>();
        stack.push(root);
        //I want to traverse left first followed by centre then right
        //
        TreeNode curNode=root;
        int counter=0;
        while (curNode!=null || stack.size()>0){
            while (curNode!=null){
                stack.push(curNode);
                curNode=curNode.left;
            }
            curNode=stack.pop();
            counter++;
            if (counter==k){
                return curNode.val;
            }
            curNode=curNode.right;
        }
        return 0;

    }
}
