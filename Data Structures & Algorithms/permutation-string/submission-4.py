class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        scount = [0] * 26
        tcount = [0] * 26
        for i in range(len(s1)):
            scount[ord(s1[i]) - ord('a')] +=1

        for j in range(len(s2)):
            tcount[ord(s2[j]) - ord('a')] +=1
            if j >= len(s1):
                tcount[ord(s2[j-len(s1)]) - ord('a')] -=1
            if scount == tcount:
                return True
        return False
    