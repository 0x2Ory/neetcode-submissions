"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldcopy = {None:None} # old new
        # okay die idee ist es quasi pro orig knoten eine n noden copie jkonte zu e
        # erstelle dann egheen wir druch die und holen uns einfach nur denkopierten gegenkonte zum velrinken

        cur = head
        while cur:
            copy = Node(cur.val)
            oldcopy[cur] = copy
            cur = cur.next
        cur = head 
        while cur: 
            copy = oldcopy[cur] # das copy ist der value also der neuue
            #jetzt müssen wir sgaen hey wohin zeigt unser alter 
            # unnd voon dem dann value nhemen und an neu üergeben
            copy.next = oldcopy[cur.next]
            copy.random = oldcopy[cur.random]
            cur = cur.next
            
        return oldcopy[head]

