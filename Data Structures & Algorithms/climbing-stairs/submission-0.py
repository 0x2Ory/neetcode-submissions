class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i):
           if i >= n:
                if i == n:
                    return True
                else: 
                    return False
           return dfs(i+1) + dfs(i+2)

        return dfs(0)