class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # was ist die Idee hier wir müssen ein SW machen das 
        # die länge von s1 hat un düber s2 läuft 
        # jetzt müssen wir cheklcne ob die charvrteilung von s1 dem von s2
        # entspricht
        # Wie vergleichen wir das bitte ? 
        # Wie bekomm eich die lokale vertielung 
        # wir durhclaufen s2 wenn s2 durch werfen wir falsch wenn es vorhe rnicht gechacth wurde
        # vil hingehen ein area machen mit s1 vertieoung 

        #if(len(s1) > len(s2)):


        char_s1=[0] * 26
        for i in range(len(s1)):
            char_s1[ord(s1[i]) - ord('a')] +=1
        
        #for i in range(len(s2)):
            
            #if( > len(s1)):


        for i in range(len(s2) - len(s1)+1):
            char_s2 = [0] * 26
            for j in range(len(s1)):      
                char_s2[ord(s2[i + j]) - ord('a')] +=1
            if char_s2 == char_s1:
                return True
        return False

        