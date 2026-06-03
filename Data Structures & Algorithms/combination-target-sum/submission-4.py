class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
     # gleicher anstaz wie vorhin 
     # also entweder nehmen wir das ding oder nicht
     # also entweder wir bleiben in desem durchgang bei i oder imnächsten i+1
     # aber das nur soalnge bis abbruch erfüllt ist
     # weöche babruch bedingungne haben wir erstaml getroffen und appenden
     # und returnen 
     # und vermutlich zu groß für target
     # als nächstes wie halt erwartet halt der backtrack algo
     # also entweder verbleiben wir mit der zahl oder wir skippen sie

    # schleifen anstz ejtztz hat einen vorteil wir könenn returnen in der schelfei wennes nun nicht passt
    # hier werden wir den skip zum nöächsten sprung i+1 and die schleife übergeben
    # len == i bruache ma auch nciht macht dei schleife ja 
    #
        nums.sort()
        res = []
        def dfs(start,cur,total):
            if target == total:
                res.append(cur.copy())
                return
            for i in range(start, len(nums)):
                if  total + nums[i] > target:
                    return
                cur.append(nums[i])
                dfs(i,cur,total = total+ nums[i])
                cur.pop()

        dfs(0,[],0)
        return res