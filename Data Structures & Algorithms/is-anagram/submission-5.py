class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        #brute force
        #s = list(s)
        #t = [ch for ch in t]
        #s.sort() 
        #t.sort()

        #for i in range(len(s)):
            #if s[i] != t[i]:
                #return False
        #return True    

        # dictionary
        #dicts = {}
        #dictt = {}
        
        #for i in range(len(s)):
            #dicts[s[i]] = dicts.get(s[i],0) +1
            #dictt[t[i]] = dictt.get(t[i],0) +1 

        #if dicts == dictt:
            #return True
        #else: return False

        # with array
        count = [0] * 26
        # for _ in range(26): count.append(0) 
        # count = [0 for _ in range(26)]:
        for chs, cht in zip(s,t):
            # alternative
            # for chs, cht in zip(s,t):
            count[ord(chs) - ord('a')] +=1
            count[ord(cht) - ord('a')] -=1

        return all(val == 0 for val in count)


