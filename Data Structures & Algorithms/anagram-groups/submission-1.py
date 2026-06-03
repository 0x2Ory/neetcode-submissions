class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # also die idee ist hier im dict den key als vertilung zu nutzen 
        # während values alle bentöigten kombinaktonen hat
        # listen können aber kein python dictiornary key sein
        # aber ein tupel lol
        res = {}
        for string in strs:
            buf = [0] * 26
            for chars in string:
                buf[ord(chars) - ord('a')]+=1
            tmp = tuple(buf)
            if tmp not in res:
                res[tmp] = []
            res[tmp].append(string)
        return [list(j) for i,j in res.items()]   
            