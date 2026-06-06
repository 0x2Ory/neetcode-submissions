class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        for j in range(len(t)):
            if s[i] == t[j]:
                if j == len(t):
                    break
                i+=1
        return i == len(s)