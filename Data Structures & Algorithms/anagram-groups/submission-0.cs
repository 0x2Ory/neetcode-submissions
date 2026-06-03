public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) 
    {
    Dictionary<string, List<string>> strstore = new Dictionary<string, List<string>>();

    foreach(string x in strs )
    {
    
        char[] chrkey = x.ToCharArray();
        Array.Sort(chrkey);
        string strkey = new string(chrkey);


        if(!strstore.ContainsKey(strkey)) strstore[strkey] = new List<string>();
        
        strstore[strkey].Add(x);

    }

    return strstore.Values.ToList();



    }
}
