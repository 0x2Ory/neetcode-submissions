class Solution:
    def findMin(self, nums: List[int]) -> int:
        # okay die Idee ist hier dadurch das Ding vom kleinsten Element aus verschoben ist muss eine 
        # eine Seite sortiert sein udn die ndere nicht das gesuche elemten ist also in der andere n unsortierten Siete


        # fangen wir wie bei Binary seach an 
        l = 0
        r =len(nums) -1

        while l < r:
            m = l +(r-l)//2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m +1
        return nums[l]