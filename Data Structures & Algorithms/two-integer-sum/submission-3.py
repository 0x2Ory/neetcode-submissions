class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        contains = {}
        for i, num in enumerate(nums):
            search_value = (target - num)
            if search_value not in contains:
                contains[num] = i
            else: 
                return [contains[search_value], i]
        
            
