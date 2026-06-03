class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        res = 0
        

        for i in range(n):
            leftmax = height[i]
            rightmax = height[i]

            for j in range(0,i):
                leftmax = max(leftmax, height[j])
            
            for k in range(i+1, n):
                rightmax = max(rightmax, height[k])

            res += min(leftmax,rightmax) - height[i]
        


        return res; 
    