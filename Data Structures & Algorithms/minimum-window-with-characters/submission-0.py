class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s)  < len(t):
            return ""   
        
        Tcontains = {}
        for i in t:
            Tcontains[i] = Tcontains.get(i,0)+1

        window = {}
        l = 0
        res = [-1,-1]
        reslen = float("infinity")
        have = 0
        need = len(t)
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0)+1

            if s[r] in Tcontains and Tcontains[s[r]] == window[s[r]]:
                have +=1

            while have == need:
                if (r-l+1 < reslen):
                    res = [l,r]
                    reslen = r-l+1
                
                if s[l] in Tcontains and Tcontains[s[l]] == window[s[l]]:
                    have -=1
                window[s[l]] -=1
                l+=1
        
        l,r = res
        if (reslen != float("infinity")):
            return s[l:r+1] 
        else:
            return ""
            #oder trinär
            #return s[l:r+1] if reslen != float("infinity") else ""