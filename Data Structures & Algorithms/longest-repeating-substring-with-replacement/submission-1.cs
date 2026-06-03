public class Solution {
    public int CharacterReplacement(string s, int k) 
    {
    int[] arr = new int[26];
    int res = 0; 
    int maxt = 0;
    int left = 0; 
    
    for(int i = 0; i < s.Length; i++)
    {
    arr[s[i] - 'A']++;
    maxt = Math.Max(maxt, arr[s[i] - 'A']);

    if(i - left +1 - maxt > k )
    {

        arr[s[left]- 'A']--;
        left++;   
    }

    res = Math.Max(res, i - left +1);
    }   
    return res; 
    }
}
