class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = {}
        for char in s1:
            countS1[char] = 1 + countS1.get(char, 0)

        need = len(countS1)
        for i in range(len(s2)):
            countS2 = {}
            cur = 0
            for j in range(i,len(s2)):
                countS2[s2[j]] = 1 + countS2.get(s2[j],0)
                if countS1.get(s2[j],0) < countS2[s2[j]]:
                    break
                if countS1.get(s2[j],0) == countS2[s2[j]]:
                    cur+=1
                if cur == need:
                    return True
        return False
    
    