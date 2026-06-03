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
 **/

public class Solution {
    public int DiameterOfBinaryTree(TreeNode root) {
        
        if(root == null) return 0; 
        int leftCall = maxHeight(root.left);
        int rightCall = maxHeight(root.right);
        int diameter = leftCall + rightCall; 
        
        int res = Math.Max(DiameterOfBinaryTree(root.left), DiameterOfBinaryTree(root.right));
        int maggi = Math.Max(diameter, res);

        return maggi;

    }

    public int maxHeight(TreeNode root)
    {
        if (root == null) return 0;
        int dia = (Math.Max(maxHeight(root.left), maxHeight(root.right))) +1;
        return dia;
    }
}
