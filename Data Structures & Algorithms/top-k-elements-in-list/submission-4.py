class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buf = {}
        for ele in nums: 
            buf[ele] = 1 + buf.get(ele,0)
        heap = []

        for num in buf.keys():
            heapq.heappush(heap, (buf[num],num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res += [heapq.heappop(heap)[1]]
        return res