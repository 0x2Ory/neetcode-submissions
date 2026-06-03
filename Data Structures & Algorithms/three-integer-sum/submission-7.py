class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()
        nums.sort()
        for i,x in enumerate(nums):
            for j,y in enumerate(nums[i+1:], start = i+1):
                for k,z in enumerate(nums[j+1:], start = j+1):
                    if nums[i] + nums[j] + nums[k] == 0:
                        if tuple([nums[i], nums[j], nums[k]]) not in res:
                            res.add(tuple([nums[i], nums[j], nums[k]]))
        return [list(x) for x in res]
