# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #was ist die Idee hier ? Wir laufen bis zum ende und returnen dann einen newhead
        # als anfang er trick -> deiser new head wir dei ganze zeit returend
        # und beim zurückgehen sagen wir dem vordermann ej bitte zeig mal auf mich !

        #zuerst die abbruhc bdignung da wir bis zum ende durhclaufen müssen
        if not head or not head.next:
            return head

        #der rekursiveslefaufruf

        new_head = self.reverseList(head.next)
# was machen wir hier ? Die Idee sich slebst bis zum Ende aufzurufen
#heißt wir gehen rein und geben head.next solange bis di eobige abbruchbedgung sagt
# ej genug der geht nemmer weiter
# wir geben das zurück und das wird das letzte elemente und neuer kopf
#jetztz müssen wir aber dem vorderman sagen ej dreh dich
# die magie head.next.next ! also vom nächsten knoten den zeiger legen wir auf uns !
        head.next.next = head
        #perfekt jetzt zeigt der vorderman auf uns
        #jetzt wirds difficlut wir sgane jetzt aber hey wir zeigen ins nichts 
        # ???
        head.next = None
        # genau weil wir jetzt rekursiv abbauen
        # der clou   wir übergebendn alten fnagpunks erneute und ziehenjetzt 
        #aber vrom stack den vorletzten kopf
        # also head2 hervor
        # head2 zeigt noch auf dei 3 !
        #also sagen wir über die 2 der drei zeig mal auf uns !
        #und legen jetzt die 2.next auf none
        return new_head

# di egrundidee lässt sich merken 1) bis zum end egehen und den nex head finden und opermanent durchreichen
# und 2) wärhndessen jedes mal dem vorderman sagen hej zeig auf mich !

# was war die Idee bei reverse die liste ? die idee war bis zum ende durch zulaufen und dann dem vorderman sagen hej zeig mal uaf mich
# wie hat man das gemacht man hat gesagt mit head.next.next = head. also vin mir (head) der vorderman ead.next zeig mal au fmich !
#Aber das ist nicht die ganze magie denn wir müssen ertsmal zum letzte ding kommen wie machen iwr das??
# reksuriv aber wie ? also bruachen wir ertsmal einen rekusirven aufurf und dazu einen abbruch 
# der abbruch sollte passierne wenn wir das ende erreicht haben aber wir müssen hier aufpasssen
# weilwir bruachen da vorletzet also wir lösen wir 
# wir gehen herutner bis zumende und holen uns head zurück warum damit 

#class Solution:
   # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

    #  #  if not head or not head.next:
     #       return head

      #  new_head = reverseList(head.next)
       # head.next.next = head
      #  head.next = none # warum machen wir das ? weil das ende der schlange auf none zeigen muss
        # und zugreifen können wir so oder so durch den vorderman

 #       return new_head


#wie würden wir das ganze iterativ machen : 
# was ist unsere Idee:
# von links nach rechts durchlaufen 
# bei jedem sich merken wo er nach vorne zeigt 
# dann sein zeiger auf none bzw prev setzen 
# der clou wir nehmen ein prev das wir none setzen 
# prev nun auf sich setzen 
# 


#prev = none
#curr = head

#while curr:
  #  tmp = curr.next
  #  curr.next = prev
  #  prev = curr
  #  curr = tmp
#return prev










