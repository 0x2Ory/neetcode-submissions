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
        #res = 0
        #for i in range(len(prices)):
            #for j in range(i,len(prices)):
                #res = max(res, prices[j] - prices[i]) 
        #return res

        # okay das war jetzt seh billig wie könnten wir das noch machen 


        # wie könnten wir d as aber noch lösen gute Frage 

       # l = 0
       # r = 1
       # maxP = 0

        #while r < len(prices):
            #if prices[l] < prices[r]:
               # profit  = prices[r] - prices[l]
              #  maxP = max(maxP, profit)
            #else:
             #   l = r
           #r+=1
        #return maxP


    # diese aufgabe ist shcwerst behindert um ehrlich zu sein 
    # die Idee ist hier die folgende wir laufe von links nach rechts und shcauen
    # obn rehctzs größer ost als links wenn das stimmt berehcnen wir das ganze per max wenn nicht ziehen
    # links auf rechts und geben am ende res aus eig genail würde ich aber nicht draufkommen 


        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy,sell)
        return maxP


#   die hier wir gehen ienmal durch das array udn merken uns denn indeze 
#   denn indeze subtrahierne wir dann von kleinsten wert denn wir gefunden haben
# denn tun wir in jedem schirtt updaten
#   gleichzeitg berehcnen wir da einmal 
        