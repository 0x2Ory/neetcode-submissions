/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
    public TreeNode InvertTree(TreeNode root) {
        //Abbruchbedingung
        if ( root==null) return null;
        TreeNode temp = new TreeNode();
        temp = InvertTree(root.left);
        root.left = InvertTree(root.right);
        root.right = temp; 
        return root;



       //RückgabeWErt
    }
}
