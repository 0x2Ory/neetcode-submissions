public class Solution {
    public bool IsPalindrome(string s)
    {
    string resstr = "";

    foreach(char t in s )
    {
    if(char.IsLetterOrDigit(t)) resstr += char.ToLower(t);
    }

    for(int i = 0; i < resstr.Length / 2; i++)
    {
    if(resstr[i]!=resstr[resstr.Length-i -1 ]) return false;
    }
    return true;
    }
}
