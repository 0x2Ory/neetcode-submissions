public class Solution {
    public int[] TwoSum(int[] nums, int target)
    {
     Dictionary<int,int> cont = new Dictionary<int, int>();

     for(int i = 0; i < nums.Length; i++)
    {
    if(cont.ContainsKey( target -nums[i] )) return new int[]{cont[ target-nums[i] ],i};
    cont[nums[i]] = i;

    }
    return null; 
    }
}
