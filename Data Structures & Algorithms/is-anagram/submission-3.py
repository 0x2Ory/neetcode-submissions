class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        bufferS, bufferT  = {}, {}
        for i in range(len(s)):
           bufferS[s[i]] = 1 + bufferS.get(s[i], 0)
           bufferT[t[i]] = 1 + bufferT.get(t[i], 0)

        return bufferS == bufferT
