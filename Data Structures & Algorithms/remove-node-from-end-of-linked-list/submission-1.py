# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # die idee wir packen die nodes in eine lsit
        nodes = []
        ptr = head
        while ptr:
            nodes.append(ptr)
            ptr = ptr.next
        # so nodes sind einer liste
        # finden wir nun heruas welchen index bruachen wir
        rmv = len(nodes)- n
        # okay nun müssen wir das elemte löschen und den pointer umstellen
        nodes[rmv-1].next = nodes[rmv].next
        return head
