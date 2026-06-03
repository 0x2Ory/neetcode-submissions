class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in  zip(position, speed )]

        # was ist die idee hier wir wollen die Zeit ausrechnen und ieg nur chekcen 
        # ob der vorherige Elemtnet gleich der zeit oder -1 hat zeiotlich

        # wie bekommen wir das erstmal heraus ? 
        # indem wir die Zeit ausrechenn wie lange e sbis zum ende braucgt 
        # Haken da das vorderste auto quasi stau machen müssen wir das berücksichtigen 
        # nalso erstmal sortiern und dann zeit berechnen 
        pair.sort(reverse=True)
        stack=[]
        for p,s in pair:
            time = ((target - p) / s)
            stack.append(time)
            # jetzt die Idee wenn das vordere element die gleiche zeit können ma es heruaslööschen 
            # weil es als fleet so doer so gilt und wir dann einzelne elemnte als fleet darstellen kann
            # warumi st das gut eine fleet uaf ein einzigesd elemnt zu reduzruen ? weil wir dadurch 
            # besser das gnaze rerturn kömnen 
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
