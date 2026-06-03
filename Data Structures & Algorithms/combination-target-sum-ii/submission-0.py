class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # was ist die grundiee hier wir vorhin 
        #backtracking zu machen und darpber dann rausfinden was bageht
        # wir müssen heir den schleifenasnatz anegheen wo ein eine for shcleife ein tiel des gnaze erldigt
        
        res = []
        candidates.sort()

        def dfs(i,cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return

            cur.append(candidates[i])
            dfs(i+1,cur, total + candidates[i])
            cur.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1,cur,total) 






        dfs(0,[],0)
        return res
