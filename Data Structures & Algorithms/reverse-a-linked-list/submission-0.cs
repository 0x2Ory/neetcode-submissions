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
    public ListNode ReverseList(ListNode head) {
   
if(head == null) return null;


    ListNode newNode = head; 
    if(head.next != null) // wenn noch was folgt
    {
        newNode  = ReverseList(head.next); // dann gehen wir auf den 
        // nächsten Knoten
        head.next.next = head;
        // den foglenden des nächsten Knoten auf sich selbst legen
    }
    head.next = null; 
return newNode; 
    }
}
