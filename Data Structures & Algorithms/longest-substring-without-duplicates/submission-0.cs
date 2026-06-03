public class Solution {
    public int LengthOfLongestSubstring(string s) 
    {
        
        int n = s.Length; 
        int maxResult = 0;

        HashSet<char> sset = new HashSet<char>();

        int walker = 0;

        for(int i = 0; i < n ; i++)
        {   
        while(sset.Contains(s[i]))
        {
        sset.Remove(s[walker]);
        walker++; 
        }   
    	sset.Add(s[i]);
        maxResult = Math.Max(maxResult,i-walker +1);
        }
        return maxResult;

    }
}
