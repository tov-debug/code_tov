#note: it is not such an easy question

"""
Problem Summary:
Find the node at which two singly linked lists intersect. If they do not intersect, return None.

Approach:
First creating a cycle if an intersection exists, by connecting the end of listA to the headB.
Then use two pointers starting from 'headA' to detect the cycle:
   The pointer'slow' is moving 1 step at a time and the pointer'fast' 2 steps. 
   Once 'slow' and 'fast' meet inside the cycle,We reset 'slow' to 'headA' and advance both pointers 1 step at a time until they meet.
   And The meeting point is the start of the cycle .
In the end restore the original structure of list A
"""
#Floyd's Cycle Detection Algorithm
# Time Complexity: O(N + M) - where N and M are the lengths of headA and headB.
# Space Complexity: O(1) - using constant extra space.
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        aptr = headA
        while aptr.next != None:
            aptr = aptr.next
        #foroming a cycle:
        aptr.next = headB

        slow , fast = headA.next, headA.next.next
        while slow != fast:
            if fast == None or fast.next == None:
                aptr.next = None
                return None
            slow = slow.next
            fast = fast.next.next
            
        slow = headA
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        #restoring:
        aptr.next = None
    
        return slow
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
