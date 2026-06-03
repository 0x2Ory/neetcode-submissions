class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range (32):
            res <<= 1
            res |= (n & 1) # das rechteste n bit und da res im an 0 stelle 0 ist der
            n >>=1
        return res
            