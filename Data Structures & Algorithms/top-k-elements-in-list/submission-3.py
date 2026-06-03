class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for nums in nums:
            count[nums] = count.get(nums,0) +1
        # Key : Anzahl
        arr = []
        for num, cnt in count.items():
            arr.append([cnt,num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res