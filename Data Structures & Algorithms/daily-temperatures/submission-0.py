class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = []


        for x in range(n):
            count = 0
            for y in range(x+1,n):
                if( temperatures[y] > temperatures[x] ):
                    count = y-x
                    break
            res.append(count)
        return res