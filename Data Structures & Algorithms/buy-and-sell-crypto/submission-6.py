class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #die idee isz wir gehen vn links nach rechts udn schauen immer. nach dem kleinsten elemnt aus
        #wennn wir das finden springen wir dagin
        res = 0
        l=0
        for r in range(len(prices)):
            if (prices[l] < prices[r]): # immer nach dem kleinsten suchen
                res = max(res,prices[r] - prices[l])
            else:
                l = r
        return res
