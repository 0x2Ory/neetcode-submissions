class Solution:
    def climbStairs(self, n: int) -> int:
# wir haben 
#       3
#      22
#     111

# können entweder 1+1+1 oder 2+1 1+2 machen -> dfs 
# abbruch bedingung die uns auffängt wenn wir n überschreiten


        def dfs(i):
            if i >= n:
                return i ==n
            return dfs(i+1) + dfs(i+2)
            
        return dfs(0)
            
