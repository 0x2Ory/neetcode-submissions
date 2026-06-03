class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        compare_string = sorted(s1)
        
        for i in range(len(s2)):
            for j in range(i, len(s2)):
                substring_2_cmp = s2[i:j+1]
                if (compare_string == sorted(substring_2_cmp)):
                    return True

        return False