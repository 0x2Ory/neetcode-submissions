class LRUCache:
    # was ist usnere Idee hier:
    # wie machen es dümmlich
    # wir hauen de dinger da rein
    # jdes mal wenn aufgerufen schauen
    # wir ob da udn auen es nach vorne wenn ja ewnn nicht nicht
    # wenn kein platz machen wir das vorderste element einfach weg
    # okay wir finden wir aber schnell das gesucht element ??
    # wir nehmen ne liste die [(key,value),]

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = []
        self.seen = set()
    def get(self, key: int) -> int:
        if key in self.seen:
            for i in range(len(self.cache)): 
                if self.cache[i][0] == key:
                    tmp = self.cache.pop(i)
                    self.cache.append([key,tmp[1]])
                    return tmp[1]
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        # wir willen wissen kennen wir das ganez shcon
        # wenn nein und platz rein und aufzählen -
        # wenn nein aber kein platz rein gehen und erstes element killen udnetc
        # wenn ja dann finden und links löschen und rehcts anhägnen
        if key not in self.seen:
            if self.capacity <= len(self.seen): # kann ich hier drhen <= 
                tmp = self.cache.pop(0)
                self.seen.remove(tmp[0])
            self.cache.append([key,value])
            self.seen.add(key)


        else:
            for i in range(len(self.cache)): 
                if self.cache[i][0] == key:
                    self.cache.pop(i)
                    self.cache.append([key,value])
