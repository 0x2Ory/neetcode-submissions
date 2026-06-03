class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # quasi die sterigerung der ersten aufgabe ohne duplicates
        #fangen wir man an mti normalen erweitreunsgsazu


        res = []
        sub = []
        nums.sort()
        def dfs(i):
            if i == len(nums):
                res.append(sub[::])
                return
            sub.append(nums[i])
            dfs(i+1)
            sub.pop()
            while i +1  < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1)

        dfs(0)
        return res