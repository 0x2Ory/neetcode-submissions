public class Solution {
    public List<List<int>> ThreeSum(int[] nums) 
    {
        Array.Sort(nums);
        List<List<int>> resList = new List<List<int>>(); 
        
        for(int i = 0; i < nums.Length ; i++)
        {
        int j = i+1;
        int k =nums.Length -1;

        if( i > 0 &&nums[i] == nums[i-1]) continue; 
        while( j < k )
        {

        if(nums[i] + nums[j]+ nums[k] == 0) 
        {
        resList.Add(new List<int> {nums[i],nums[j],nums[k]});
        j++; 
        k--; 
        while(j  < k && nums[j] == nums [j-1]) j++; 
        }
        else if ( nums[i] + nums[j]+ nums[k] < 0 ) j++;
        else k--;
        

        }

        }
    return resList; 
    }
     
        
    }

