public class Solution {
    public List<List<int>> ThreeSum(int[] nums) 
    {
        Array.Sort(nums);
        List<List<int>> resList = new List<List<int>>(); 
        int k =nums.Length -1;
        
        for(int i = 0; i < nums.Length ; i++)
        {
        int j = i+1;
        
        while( j < k )
        {

        if(nums[i] + nums[j]+ nums[k] == 0) 
        {
        resList.Add(new List<int> {nums[i],nums[j],nums[k]});
        j++; 
        k--; 
        }
        else if ( nums[i] + nums[j]+ nums[k] < 0 ) j++;
        else k--;
        

        }

        }
    return resList; 
    }
     
        
    }

