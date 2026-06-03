public class Solution {
    public int LongestConsecutive(int[] nums) 
    {  
    HashSet<int> hp = new HashSet<int>(nums);
    int reslen = 0; 
    
    foreach(int num in nums)
    {

    if(!hp.Contains(num - 1))
    {
     int length = 1; 
        while(hp.Contains(num+length))
        {
            length++; 
        }
        reslen = Math.Max(reslen, length);
    }
    }

    return reslen; 
    }
    
    
    }

