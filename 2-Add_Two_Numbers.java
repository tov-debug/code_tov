/**
 Problem Summary:
 to add two numbers that represented backward in a list(node for each digit)

 Approach:
 2th graded addition with a carry.
  */

//Simple pass over the two lists adding one after another.
//Time complexity: O(M+N)- where N & M are the sizes of the list.
//Space complexity: O(max(N,M)) - for storing the result.
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int remain = 0;
        ListNode res = new ListNode();
        ListNode pt = res;
        int add;

        //looping over both lists to preform the adding one by one
        while (l1 != null && l2 != null)
        {
            add = l1.val + l2.val + remain;
            pt.next = new ListNode(add%10);// in base 10 only digit 0-9
            remain = add/10;//can be 1 or 0
            //moving on:
            l1 = l1.next;
            l2 = l2.next;
            pt =pt.next;
        }

        //if there left in l1
        while(l1 != null)
        {
            add = l1.val + remain;
            pt.next = new ListNode(add%10);
            remain = add / 10;
            l1 = l1.next;
            pt =pt.next;
        }

         //if there left in l2
        while(l2 != null)
        {
            add = l2.val + remain;
             pt.next = new ListNode(add%10);
            remain = add / 10;
            l2 = l2.next;
            pt =pt.next;

        }

        //extra remain
        if(remain != 0) 
            pt.next = new ListNode(remain);
        
        return res.next;//skip dummy head node
    }
}


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */