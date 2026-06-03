class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # die idee ist von links nach rechts zu laufne bis wir dei summe haben
        # danach von links das fenster zu verkleinern
        # wie berechnen wir hier dei summe des fenster -> supe einfach die berechenne einfach
        # mit der for die summe


        l = 0 
        sumsum = 0
        res = float("inf")
        for r in range(len(nums)):
            sumsum +=nums[r]

            while (target <= sumsum ):
                sumsum -= nums[l]
                res = min(res, r-l+1)
                l+=1
            
        return 0 if res == float("inf") else res
