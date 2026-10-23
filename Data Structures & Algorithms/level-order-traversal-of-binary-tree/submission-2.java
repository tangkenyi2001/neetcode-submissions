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
    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root==null){
            return new ArrayList<>();
        }
        Queue <TreeNode> queue = new ArrayDeque<>();
        List<List<Integer>> res= new ArrayList<>();
        queue.add(root);
        while (queue.size()>0){
            List<Integer> curRes= new ArrayList<>();
            int queueLength=queue.size();
            for (int i=0;i<queueLength;i++){
                TreeNode curNode=queue.poll();
                if (curNode.left!=null){
                    queue.add(curNode.left);
                }
                if (curNode.right!=null){
                    queue.add(curNode.right);
                }
                curRes.add(curNode.val);
            }
            res.add(curRes);
        }
        return res;
    }
}
