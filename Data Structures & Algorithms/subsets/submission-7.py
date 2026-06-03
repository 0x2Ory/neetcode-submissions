class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #es gibt zwie ansätze das zulösen hier 
        # erster: Erweiterungsansatz
        # bascially die ist wir nehmen die Zahl oder nicht und versuchen es
        # speiche  rn tun wir jedes mal wenn wir da ende eines pfades gefunend haben 
        # zwieter anstaz per schleeife

        res = []
        sub = []
        def dfs(start):
            res.append(sub.copy())
            for i in range(start,len(nums)):
                sub.append(nums[i])
                dfs(i+1)
                sub.pop()


        dfs(0)
        return res





        
        
