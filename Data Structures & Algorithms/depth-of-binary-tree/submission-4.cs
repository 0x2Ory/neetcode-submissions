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
// oaky komishce Idee da wir rekusriv nicht arbeiten müssen wir uns bei bfs 
// ja iwie immernach unten schuafen indem wir dei neuen elmente rechts hinzufügen
//jedtzt merken wir uns ienfahc ide neuen elemtne und laufen nur deise anzahl durch 


public class Solution {
    public int MaxDepth(TreeNode root) 
    {
        if( root == null) return 0;
        Queue<TreeNode> q = new Queue<TreeNode>();
        q.Enqueue(root);
        int count = 0;
        while ( q.Count > 0)
        {
            int size = q.Count;

            for( int i =0; i <size; i++)
            {
                TreeNode temp = q.Dequeue();
                if (temp.left != null) q.Enqueue(temp.left);
                if (temp.right != null) q.Enqueue(temp.right);
            }
            count ++;

        }
        return count;

    }
}
