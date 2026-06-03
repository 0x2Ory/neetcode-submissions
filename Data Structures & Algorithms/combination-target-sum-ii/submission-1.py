class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # was ist die grundiee hier wir vorhin 
        #backtracking zu machen und darpber dann rausfinden was bageht
        # wir müssen heir den schleifenasnatz anegheen wo ein eine for shcleife ein tiel des gnaze erldigt
        
        res = []
        candidates.sort()
        def dfs(j,path,cur):
            if cur == target:
                res.append(path.copy())
                return 
            for i in range(j,len(candidates)):
                if i > j and candidates[i] == candidates[i-1]:
                    continue
                if cur + candidates[i] > target:
                    break

                path.append(candidates[i])
                dfs(i+1, path, cur+candidates[i])
                path.pop()
    
        dfs(0,[],0)
        return res
