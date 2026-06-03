public class Solution {

    public string Encode(IList<string> strs) 
    {
        return string.Concat(strs.SelectMany( s => $"{s.Length}#{s}"));
    }

    public List<string> Decode(string s)
    {
    List<string> res = new List<string>();
    for(int i = 0; i < s.Length;)
    {
        int j = i; 
        
        while(s[j] != '#')
        {
            ++j;
        }

        int.TryParse(s.Substring(i, j-i), out var len);
        j++;
        res.Add(s.Substring(j,len));
        i = j+len;
    }
    
return res;


   }
}
