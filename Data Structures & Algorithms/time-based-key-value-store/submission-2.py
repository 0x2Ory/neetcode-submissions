class TimeMap:

    # was passiert hier: 
    # wir wollen ein time dict haben das zu einem key value uach noch eine zeit speicher
    # anahnd der wie die zeiten soritern müssne
    # wichtig is hier die get eig nur die get -> die soll nämlich für den gebenen timestamp
    # das zu dem zeitpunk neuste bzw nähste even fidnen. also zu der tiemstamp relativ das in der ver
    # vergnageheit am kürzseteb entferne objekt also quasi das mti delta t kelin
    # heißt für uns wir müssen das nach der zeit suchen die time <= target target sit am wneisgte abstand hat

    # welch enöglichekiten haben wir das zu machen
    # einfahc nur die werte ienspeichern und dann sichen nach dem größtne objekt kleiner asl target
    # ads halt bruteforce und nciht sher peromrnant
    #alöterantive ? da wir die zeitlich abspeichern können sind sie dotiet udn wir könenn mit bianry sort 
    # das ganze lösen !
    # wie wir speichern für jeden key eien list 
    # dann können wie die list heruasnehmen und bianry search uaf die list naweden 


    def __init__(self):
        self.store= {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        lst = self.store.get(key,[])
        l = 0
        r = len(lst) -1
        while l <= r:
            m =l + ((r-l)//2)
            if lst[m][1] <= timestamp:
                res = lst[m][0]
                l = m+1
            else:
                r = m -1

        return res


