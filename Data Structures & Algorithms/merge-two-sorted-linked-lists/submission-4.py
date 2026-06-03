# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# was ist die Idee hier:
# wir gehen durhc die länge der liste durch udn schaune
# hej welche listenwert ist kleiner ?
# finden wir denn rufen wir dei funtkion nochmal auf aber nun mit dem nachgehenden wert
# wie linken bzw returne wir das gnaze jetzt zusammen 
# wenn du größer als ich 







class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            # die Idee
            if list1 is None:
                return list2

            if list2 is None:
                return list1

            if list1.val <= list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2


           # 1,3, 
            #24

            #stack : 1,(3,2) - 2, (3,4) - 3(none,4) - return 4 - wir sagen hier dann
            #3 -> 4 - returnen 3->4 - 2-> 3->4 _> returnen jetzt 2 und zurück oben auf list 1 next