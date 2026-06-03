public class Solution {
    public bool hasDuplicate(int[] nums)
{
    HashSet<int> ConCon = new HashSet<int>(); 
    
    foreach(int x in nums)
    {

    if(ConCon.Contains(x)) return true;
    else ConCon.Add(x);
    }
    return false; 
}
}
