class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # fangen wir mit brute force ,an:
        # was wollen wir gue eigbet,ich wir wollen aus der lsite das arra ymit dem grlßten gewinn haben 
        # also da wo t-s denn größten gewinn hergibt
        # wir bekommen wir das him wir craalen einmal von links nach rechts durch 
        # for i in range(len(prices)):
        #   for j in range(i,len(prices)):
        #. nun müssen wir schauenhey wie bekommen wir den verkaufswert ??
        # ganze einfach wir machen ein max( max, xx) x ist beim bruteforcen 
        # die diskrepanz zwischen i-j und shcauen das der größte wert o
        #
        res = 0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                res = max(res, prices[j] - prices[i]) 
        return res