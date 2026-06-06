class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        val = 0
        for i in range(len(nums)-k+1):
            for j in range(i,i+k):
                val = max(nums[j],val)
            res.append(val)
            val = 0 
        return res
