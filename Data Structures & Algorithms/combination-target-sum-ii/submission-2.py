class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        def dfs(start,total):
            if target == total:
                res.append(sub[::])
                return
            if start >= len(candidates) or total > target:
                return 
            sub.append(candidates[start])
            dfs(start+1,total +candidates[start])
            sub.pop()
            while start+1 < len(candidates) and (candidates[start] == candidates[start+1]):
                start+=1
            dfs(start+1,total)


        dfs(0,0)
        return res 