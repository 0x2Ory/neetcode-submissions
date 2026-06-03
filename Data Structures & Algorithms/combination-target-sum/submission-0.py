class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #hier ist die Abbruchbedinung zu vorhin nicht in rnage oder größer gleich
        # sonder trifft er das target oder nicht
        # zwei fälel wenn er trift und wenn er drübr geht da wir ja speichen müssne das ergenis

        # wir vorhin die idee entweder nummt er das derzeitige lemente oder das nächste

        res = []

        def dfs(i,cur,total):

            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            cur.append(nums[i])
            dfs(i,cur,total+nums[i])
            cur.pop()
            dfs(i+1,cur,total)

        dfs(0,[],0)
        return res 
