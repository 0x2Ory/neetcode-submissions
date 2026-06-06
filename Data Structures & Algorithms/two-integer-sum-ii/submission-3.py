class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        buf = {}
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if tmp in buf:
                return [buf[tmp]+1,i+1]
            buf[numbers[i]] = i
        return []