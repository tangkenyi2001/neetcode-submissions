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
    public boolean validBST(TreeNode root,int lowerlimit,int upperlimit){
        if (root==null){
            return true;
        }
        if (lowerlimit>=root.val || root.val>=upperlimit){
            return false;
        }

        boolean left=validBST(root.left,lowerlimit,root.val);
        boolean right=validBST(root.right,root.val,upperlimit);

        return left && right;

    }
    public boolean isValidBST(TreeNode root) {
        return validBST(root,-1*Integer.MAX_VALUE,Integer.MAX_VALUE);

    }
}
