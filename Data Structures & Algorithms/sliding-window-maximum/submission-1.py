class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        val = float("-infinity")
        for i in range(len(nums)-k+1):
            val = nums[i]
            for j in range(i,i+k):
                val = max(nums[j],val)
            res.append(val)
        return res
