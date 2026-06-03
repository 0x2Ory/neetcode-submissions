/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
 
public class Solution {
    public ListNode MergeTwoLists(ListNode list1, ListNode list2) {


    ListNode dummy = new ListNode(0);
    ListNode node = dummy; 

    while(list1 != null && list2 != null)
    {

        if(list1.val < list2.val)
            {
                node.next = list1; // trage den list1node als nächsten node ein
                list1 = list1.next; // iteriere die liste 1 um eins weiter
            }
        else
            {
                node.next = list2; // trage den List2 als folgenden Node ein 
                list2 = list2.next;
            }
            node = node.next; // iteriere dei Liste um eins weiter
    }

    if (list1 != null)
    {
        node.next = list1; 
    }
    else node.next = list2;


    return dummy.next;
    }
}