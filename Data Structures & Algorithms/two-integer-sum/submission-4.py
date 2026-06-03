class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # brute force
        #for i in range(len(nums)):
         #   for j in range(i+1, len(nums)):
          #      if nums[j] == nums[i]:
           #         continue
              #  if (nums[j] + nums[i] == target):
            ##        return [i,j]
        #return [0,0]

        buf = {}

        for i in range(len(nums)):
            
            if (target - nums[i]) in buf:
                return [buf[target-nums[i]],i]
            
            if nums[i] not in buf: 
                buf[nums[i]] = i
        
        return [0,0]



