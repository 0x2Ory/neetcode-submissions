class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        sub = []

        def dfs(start,toal):
            if toal == target:
                res.append(sub[::])
                return 
            for i in range(start, len(nums)):
                if toal +nums[i] > target:
                    return
                sub.append(nums[i])
                dfs(i,toal + nums[i])
                sub.pop()


        dfs(0,0)
        return res