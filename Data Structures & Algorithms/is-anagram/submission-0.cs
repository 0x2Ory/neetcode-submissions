public class Solution {
    public bool IsAnagram(string s, string t)
    {
        if(s.Length != t.Length) return false; 
    
        int[] h = new int[26]; 

    for(int i = 0; i < s.Length; i++)
    {
        h[s[i] - 'a']++;
        h[t[i] - 'a']--;
    }

    foreach(int x in h)
    {
        if(x != 0) 
        {return false;}
    }

    return true; 
    }
}
