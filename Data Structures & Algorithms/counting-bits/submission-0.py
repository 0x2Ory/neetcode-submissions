class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n+1):
            buf = 0
            for i in range(32):
              if num & (1 << i):
                buf+=1
            res.append(buf)
        return res