public class Solution {
    public int MaxSubArray(int[] nums) {

        int n = nums.Length;
        int[] dp = (int[])nums.Clone();
        for ( int i = 1 ; i < n; i++)
        {
            dp[i] = Math.Max(nums[i], nums[i]+ dp[i-1]);
        }
        int res = nums[0];
        
        foreach (int sum in dp)
        {
            res = Math.Max(res,sum);
        }

        return res; 

    }
}