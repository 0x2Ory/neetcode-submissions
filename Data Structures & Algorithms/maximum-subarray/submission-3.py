class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #idee wenn sukme eh unter null ist bruache ma sine eh nicht und können verwerfen und eue nafganen :
        res = nums[0]
        tmp = 0
        for num in nums:
            if tmp < 0:
                tmp  = 0
            tmp+=num
            res = max(res, tmp)
        return res