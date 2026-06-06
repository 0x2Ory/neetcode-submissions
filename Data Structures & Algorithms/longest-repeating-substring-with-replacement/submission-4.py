class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        i = 0
        contains = {}
        maxfreq = 0
        for j in range(len(s)):
            contains[s[j]] = (contains.get(s[j],0)+1)
            maxfreq = max(maxfreq, contains[s[j]])
            while((j-i+1)-maxfreq) > k:
                contains[s[i]] = -1
                i+=1
            res = max(res, j-i+1)        
        return res