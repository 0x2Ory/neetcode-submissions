class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #hier ist die Abbruchbedinung zu vorhin nicht in rnage oder größer gleich
        # sonder trifft er das target oder nicht
        # zwei fälel wenn er trift und wenn er drübr geht da wir ja speichen müssne das ergenis

        # wir vorhin die idee entweder nummt er das derzeitige lemente oder das nächste




        res = []
        nums.sort()

        def dfs(i,cur,total):
            if total == target:
                res.append(cur.copy())
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return 
                cur.append(nums[j])
                dfs(j,cur,total+nums[j])
                cur.pop()
        dfs(0,[],0)
        return res 
