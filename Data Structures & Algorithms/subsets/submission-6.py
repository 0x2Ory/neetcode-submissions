class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #es gibt zwie ansätze das zulösen hier 
        # erster: Erweiterungsansatz
        # bascially die ist wir nehmen die Zahl oder nicht und versuchen es
        # speichern tun wir jedes mal wenn wir da ende eines pfades gefunend haben 


        res = []
        sub = []
        def dfs(i):
            if(i >= len(nums) ):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            dfs(i+1) #take it
            sub.pop() #backtracking
            dfs(i+1) # ergibt mit bnackltracking die situation nimmt nicht


        dfs(0)
        return res





        
        
