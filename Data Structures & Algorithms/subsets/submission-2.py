class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        #res+=[[]]

        for num in nums:
            size = len(res)
            for i in range(size):
                res+= [[num] + res[i]]
                #res.append([num] + res[i])
        return res