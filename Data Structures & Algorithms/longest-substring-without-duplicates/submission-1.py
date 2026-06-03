class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        contains = set()
        for i in range(len(s)):
            if s[i] not in contains:
                contains.add(s[i])
                res = max(res, i - l + 1)
            else:
                while s[i] in contains:
                    contains.remove(s[l])
                    l+=1
                contains.add(s[i])
        return res