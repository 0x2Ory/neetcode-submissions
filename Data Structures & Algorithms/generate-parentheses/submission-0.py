class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sub = []    


        def dfs(nop,ncl):
            if nop == ncl == n:
                res.append("".join(sub))
                return
            
            if nop < n:
                sub.append("(")
                dfs(nop+1, ncl)
                sub.pop()
            if ncl < nop:
                sub.append(")")
                dfs(nop, ncl+1)
                sub.pop()

#


        dfs(0,0)
        return res


        