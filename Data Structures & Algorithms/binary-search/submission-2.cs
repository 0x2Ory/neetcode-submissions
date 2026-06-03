public class Solution {
    public int Search(int[] nums, int target) 
    {
        int leftbound = 0;
        int rightbound = nums.Length-1; 
        
        while(leftbound <= rightbound)
        {
            int m = leftbound +((rightbound - leftbound) / 2) ;
            if(nums[m] < target) leftbound = m+1;
            else if (nums[m] > target) rightbound = m-1;
            else return m;

        }
        return -1; 

    }
}
