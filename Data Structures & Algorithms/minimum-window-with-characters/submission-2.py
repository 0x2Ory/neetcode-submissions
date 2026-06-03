class Solution:
    def minWindow(self, s: str, t: str) -> str:
        

        # die ist es hier in dem einem stringvom andren string alle 
        # chars zu finden und das im klienst möglichen fenster
        # also lsdiing window

        # die also bei o(N) von links anch rehcts durczukaufne und dabei
        # zu schaien was ist wan drinnen
        # aslo erstmal eine schleife mit zwei pointern dee eien 
        # fängt mit r an und schaut wie lange bis wir alle drinnenb haben 
        # dann gehen wir hin und schuane wie lange wir mit links nach ziehen können 
        # bei einem vlaidne fenster


        # es steht da wenn ein solche substring nciht existert gib einene leerne uas

        # also erstmal den edge case abdenken :
        # gute die grundiee sthet nun also solange suchen bis wir die chars finden 
        # Problem: wie machen wir den rest wir erkennen wir erstmakl welche charsw wir suchen 
        # und oballe drinenn ist -> er sagt oben alle duplikate also ghet kein hashset sonder wir bruach
        # eine hashmap auch bekannt also Dictuonary
        # nun haben wir mit tdict alle bneeötigten chars im dictioanry gesammelt
        # wie raffen wir jetzt aber das von usne gezogene sliding window fenster alle chars enthält die wir haben wollen ??
        # wir müssen entweder ein zweites dict machen und da lles herualöschen wenn wir was sehen
        # und permant vergleichen oder
        # oder wir machen wein zweites wo wir nur rein hinzufügen da sind die zwie ansätze

        # okay nachdem wir das gelöst haben 
        # 

        # wir gehen wir nun weiter voran mit usnerr schleife ???
        # wir gehen nach rechts und merken und jedes mal das derzeitge elemnt und knallen
        # es in die in unser wdict 0)
        # danach werden wir schauen müssen ob wir alle zeichen getroffen haben 1)
        # und 2) und von links das fenster verkleienr müssen
        # 3) soiwe das kleinste fenster fidnen müssen -> tricky da iwas max und min ist

        # fangen wir mit 0 an das ist straiht forward das nur dict und befüllen vom derzeitgne elemnt
        # 1, 23 und sin schon ander kalibere


        # jetzt kommen wir zu was intersantemum zu merken haben wir das richtige fenster erwischt
        # wir können dei gröpe eines dicts bestimmen also alle werte bestommen
        # einfach len von tdict -> dei anzahl die wir bruachen mindenst also usner need
        # wenn wir was min needen haben wir uach have aösp have wie viele chcars wir derzeit haben
        # und jetzt kommt er tricj wir sagen hej ist s[r] derzeztig in dictt und genau so oft in unserem wfenster 
        # dann hamma genug da !!!
        # also if s[r] in tdict -> für ist der derzeitge wert überhuapt gesucht
        # + hamma wa genug da mit wdict[s[r]] == tdict[s[r]]
        #if s[r] in tdict and wdict[s[r]] == tdict[s[r]]:
        #    have+=1
        # das kann etzt ruhig vor sich in tuckern und alle suchen 
        # was passiert wenn wir alle gufndeien aben asp whiel have ?== need
        # dann erfüllen wir hiermit den ersten punkt haben wir alle zeichen eghfudnen 
        # in diese bedingung müssen wir dann von links das fenster verkleinern und uns de kleinste kombi speicherhn
        
        # aöso einmal aus wdict löschenund einmal noch verklöiern

        #okay letztes grßes problem wie specern wir das lkeinste fenstere gi 
        # wir ghen hin und bauen in der while have == need eine bedingung ein dei die abspehcert den kleisnten wetrt
        # amcht ja auch sinn in deiser while ist die welt in orndung und wir itereiren ja danach nachrechts von links
        # sollte im nächetsn sdurhcngng die welt noch in orndung sein speichern wir das 
        # wie specher wir aber dden besten zeitpunkt wie immer r-l+1
        # ohoho wir shcuaen was kleiner ist ! also brauchen wi r im gegesatz zui may wo wir mit null isntialsiern 
        #dn vergleichswert einen hohen vergelichswert was nehmen wir dazu am betsen ein float("infintiy
        #") ja ja python manchmal bist du einw eirdo siehe du und diene maxhepa kaka

        #da wir reslene bruachen als vergleifchwert bruachen wir einen res 
        # okay fast zu endee wir hauen uns neustes ergebnis un res rein und merken und di eneuste kleine
        # länge in. reslen 

        # fast fertig jetzt müssen nur noch checken ob alles in habe und need drinnen ist:
        # beim links gehen natürlich also
        # of s[l] in tdict -> ob das didng überhaupt dirnne ist
        # und für die anzahl drinenn ist also ist unser fenster wert kleiner als der bentöigt wert
        # was nach adam riese egbit wdict[s[l]] < tdict[s[l]]
        # -> if s[l] in tdict and wdict[s[l]] < tdict[s[l]]:
        # wir sind nun durch und mpssen hetzt nur noch das diing übergebne hurra

        if len(t) == 0:
            # oder auch t == ""
            return ""

        l = 0
        wdict = {}
        tdict = {}
        res = [-1,-1]
        reslen = float("infinity")
        have = 0
        
        for char in t:
            tdict[char] = tdict.get(char, 0) +1

        need = len(tdict)

        for r in range (len(s)):
            wdict[s[r]] = wdict.get(s[r],0)+1

            if s[r] in tdict and wdict[s[r]] == tdict[s[r]]:
                have+=1


            while have == need:
                if ( r-l +1) < reslen:
                    res = [l,r]
                    reslen = r-l+1
                wdict[s[l]] -= 1


                if s[l] in tdict and wdict[s[l]] < tdict[s[l]]:
                    have -=1
                l +=1
        l,r = res
        if reslen != float("infinity") :
            return s[l:r+1]
        else:
            return ""


