class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        for i in range(len(s)):
            contains = {}
            maxfreq= 0
            for j in range(i,len(s)):
                contains[s[j]] = (contains.get(s[j],0)+1)
                maxfreq = max(maxfreq, contains[s[j]])
                if((j-i+1)-maxfreq) <= k:
                    res = max(res, j-i+1)        
        return res