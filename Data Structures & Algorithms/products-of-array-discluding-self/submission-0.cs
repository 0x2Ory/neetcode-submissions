public class Solution {
    public int[] ProductExceptSelf(int[] nums)
    {
        int len = nums.Length; 
        int[] res = new int [len];

        for(int i = 0; i < len; i++)
        {
            int prod = 1; 
            for(int j = 0; j< len; j++)
            {
             if(i != j) prod *=nums[j];
            }
            res[i] = prod;
        }

    return res; 
    }
}
