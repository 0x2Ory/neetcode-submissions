class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        for i in range(len(s)):
            seen = {}
            most = 0
            for j in range(i,len(s)):
                seen[s[j]] = seen.get(s[j], 0)+1
                most = max(most,seen[s[j]])
                if (j-i+1 - most)  <= k:
                    res = max(res,j-i+1)
        return res