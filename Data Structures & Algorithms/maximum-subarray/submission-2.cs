public class Solution {
    public int MaxSubArray(int[] nums) {
        int maxsub = nums[0];
        int currsum = 0;

        foreach(int num in nums)
        {
            if(currsum < 0)
            {
                currsum = 0;
            }

            currsum += num;
            maxsub = Math.Max(maxsub, currsum);
        }
        return maxsub;
    }
}