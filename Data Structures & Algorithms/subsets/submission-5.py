class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # es gibt zwei Ansätze wie man das ganze hier löst:
        # Schleifen und Erweiterungsansatz bzw binäres nehmen und nicht nehmen
        # Die GrundIdee bei solchen Aufgaben-> Backtracking einfach jeden Möglichkeit ausprobieren
        # Heruntergebrochen heißt das entweder wir probeiren die Kombination oder nicht
        # -> entweder wir nehmen die nächste Zahl oder nicht
        # fangen wir mit binär an
        # Binär -> Wir gehen rein und nehmen die Zahl und nehmen einmal die Zahl nicht
        # wie stellen wir aber den Zustand nach nehmen die Zahl, für wir nehmen die Zhal nicht wieder her
        # mit POP ! das tiefer gehen selbst quasi das dfs heißt für uns:


        #res = []
        #sub = []
        #def dfs(i):

            #if i >=(len(nums)):
                #res.append(sub.copy())
                #return
            #sub.append(nums[i])
            #dfs(i+1) #wir nehmen die Zahl / den Pfad # nicht überlegen was passiert sonder nur das er nahc unten geht
            #sub.pop() #backtracking
            #dfs(i+1) #wir nehmen die Zhal nicht


        #dfs(0)
        #return res

        # okay das grundgerüst steht aber wie tracken wir was abgeht ??
        # ganz einfach jedes mal wenn wir dei Länge bzw die Kombination exhausted haben
        # als praktisch am Blatt des Entscheidungsbaumes stehen speichen wir dei Kombi 
        # das iwrd unsere abbruchmöglichkeit -> wie machen wir das 
        # indem wir chcken ob es die len >= hat !



        # jetzt der schleifen anstatz der ist gradliniger
        #statt einen ich nehme den Path nicht zu implemntierne und uqai damit dei gespeiglete seite des 
        # baumes zu implemntiren soll das einfach ne for schleife erledigen 

        res = []
        sub = []

        def dfs(start):

            res.append(sub.copy()) # hier appenden wir res davor weil
            # er ja unten abbechen würde -> gleiche IDee wie oben
            #speicher dieletzte positoin
            for i in range(start, len(nums)): # wird beim zurückgehen einfach für den restlichen
            # liegen geblebenden Part sorgen 
                sub.append(nums[i])
                #gehe jetzt tiefer
                dfs(i+1)
                sub.pop() # backtrcke




        dfs(0)
        return res




        
        
