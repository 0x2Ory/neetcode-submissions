class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0 
        res = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0)+1
            maxf = max(maxf,count[s[r]])

            # aber wann 
            # wenn uínserem fentser - die maxiamle anzahl größer
            # ist als k dann haben wir mehr ret als erluabt
            # also  r-l+1 - maxf > k
            while (r-l)+1 - maxf > k:
                count[s[l]]-=1
                l+=1 
            res = max(res, (r-l)+1)
        return res