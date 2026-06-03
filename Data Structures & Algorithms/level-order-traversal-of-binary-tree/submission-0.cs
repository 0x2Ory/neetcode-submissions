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
    public List<List<int>> LevelOrder(TreeNode root) {
        // folgende Idee: wir mahcen das mit breitensuche
        // jedes mall wenn wir durchegehen duch eine tiefe isnatnz 
        // poppen wir das einfach in in ne lsute und fertgi 
        List<List<int>> res = new List<List<int>>();
        if(root == null) return res;
        Queue<TreeNode> buffer = new Queue<TreeNode>();
        buffer.Enqueue(root); 
        while (buffer.Count > 0)
        {
        List<int> cont = new List <int>();
        int threshold = buffer.Count;
        for(int i = 0; i < threshold; i++)
        {
            TreeNode node = buffer.Dequeue();
            if(node != null)
            {
            cont.Add(node.val);   
            if(node.left != null) buffer.Enqueue(node.left);
            if(node.right != null) buffer.Enqueue(node.right);
            }
        }
        if(cont.Count > 0)
        {
            res.Add(cont);
        }


        }
        return res; 


    }
}
