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
        if (root == null) return null; 

        Queue<TreeNode> speicher = new Queue<TreeNode>();
        speicher.Enqueue(root);
        while (speicher.Count > 0)
        {        
            TreeNode node = speicher.Dequeue();
            TreeNode temp = node.left;
            node.left = node.right;
            node.right = temp;
            if( node.left != null) speicher.Enqueue(node.left);
            if( node.right!= null) speicher.Enqueue(node.right);
        }
        return root; 

    }
}
