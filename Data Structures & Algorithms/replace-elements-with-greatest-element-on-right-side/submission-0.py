class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n 
        for i in range(n):
            maxele = -1
            for j in range(i+1, n):
                maxele = max(maxele, arr[j])
            ans[i] = maxele
        return ans