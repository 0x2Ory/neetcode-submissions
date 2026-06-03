public class Solution {
    public int Trap(int[] height) 
    {
       //if(height == null || height.Length == 0) return 0; 
        int n = height.Length;
        int res = 0; 

        for (int i = 0; i < n; i++)
        {
            int lefth = height[i];
            int righth = height[i];

            for (int j = 0; j < i; j++)
            {
                lefth = Math.Max(lefth, height[j]);
            }
            for (int k= i+1; k < n; k++)
            {
                righth = Math.Max(righth, height[k]);
            }
            res += (Math.Min(lefth,righth)) - height[i];
        }


        return res; 
    }
}
