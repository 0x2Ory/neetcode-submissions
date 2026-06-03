# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(0)
        cur = res 
        while True:
            mini = -1

            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if mini == -1 or lists[mini].val > lists[i].val:
                    mini = i
                
            if mini == -1:
                break

            cur.next = lists[mini]
            lists[mini] = lists[mini].next 
            cur = cur.next
        return res.next