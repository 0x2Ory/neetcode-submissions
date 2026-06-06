class Solution:
    def search(self, nums: List[int], target: int) -> int:
     #   l = 0
        #r = len(nums)-1

        #while l<=r:
          #  mid = l+((r-l)//2)
           # if target == nums[mid]:
            #    return mid
            # wenn das hier wahr dann ist der linke teil sortert

        #        if target > nums[mid] or target < nums[l]:
         #           l = mid + 1
            # wenn zielwert größer als mid oder kleiner als der linkerpoint
            # versetze links eins anch rechts
       #         else:
      #              r = mid - 1
            # wenn das nicht der ffall stelle den rechten pointer links von mid
        # wenn das hier eintritt ist der Rechte Teil sortiert
            #else: # also wenn der wert im linken Zeiger größer ist als der der Mitte
             #   if target < nums[mid] or target > nums[r]:
                    # wenn ziel werd werd kleiner als mid
                    # oder ziel größer asl rechts
                # sonst
              #  else:
               #     l = mid+1   
     #   return - 1

        # 345612 -> 1
        # 1) wir suchen den sortierten Tiel der Liste
        #scaheun ob im sortiern tield er liste da tagret größer als mid ist doer kliener als 
        # links und eghen dann in enren andere teil 

        # also wir suchen den sortierten teil und schauen ob usner gesuchter wert hier ist oder
        # eventuell die randwerte mit und links übertorff tund folglich osmit wo anders liegt 
        # sollte das der fall sein vershcieben wir das fenste rin den nicht sortierten teil.

        # fogllich ist hier die grundidee versuch dich am sortiernten beriech festzhalten und fidne den so
        #sortieren teil dann schaue ob der zielwert in deisem bereichen ist 
        # wenn nciht setz den rahmen in den andern bereich um

        r = len (nums)-1
        l = 0
        while l<=r:
            m = l + ((r-l) //2)
            if target == nums[m]:
                return m

            if nums[m] < nums[r]:
                if nums[l] < target <  nums[r]:
                    l = m+1
                else:
                    r = m-1
            else:
                if nums[l] <  target <  nums[m]:
                    r = m-1
                else:
                    l = m+1

        return -1


        # 1) Suche sorteirten Intervall
        # 2) Check ob Target im derzeitgen Intervall
        # 3) Wenn nicht stelle Rahmen auf den andern inervall ein 
