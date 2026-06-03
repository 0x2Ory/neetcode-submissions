public class Solution {
    public bool IsAnagram(string s, string t)
    {
    if(s.Length != t.Length) return false; 
    char[] x = s.ToCharArray();
    char[] y = t.ToCharArray();

    Array.Sort(x);
    Array.Sort(y);

    return Enumerable.SequenceEqual(x,y);
    // return x.SequenceEqual(y);
      
}
}