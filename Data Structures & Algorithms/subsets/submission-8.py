class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #zwei ansätze schleife doer erweiterung 
        res = []
        cur = []
        def dfs(start):
            if(start >= len(nums)):
                res.append(cur[::])
                return
            cur.append(nums[start])
            dfs(start+1)
            cur.pop()
            dfs(start+1)
        dfs(0)
        return res 




        
        
