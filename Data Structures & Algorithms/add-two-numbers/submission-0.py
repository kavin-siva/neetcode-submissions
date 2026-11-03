# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        # Loop continues while there are nodes to process OR a leftover carry
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total sum and update carry
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            digit = total_sum % 10
            
            # Create a new node with the single-digit value
            curr.next = ListNode(digit)
            curr = curr.next
            
            # Advance the input lists safely
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next

        