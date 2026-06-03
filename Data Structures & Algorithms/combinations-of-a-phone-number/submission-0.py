class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []
        res = []

        map = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }


        def dfs(i,buf):
            if len(buf) == len(digits):
                res.append(buf)
                return 
            for c in map[digits[i]]:
                dfs(i+1,buf+c)
                buf.rstrip()

            
        dfs(0,"")
        return res