class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # Create a dummy node to seamlessly anchor the head of the new list
        dummy = ListNode()
        tail = dummy
        
        # Traverse both lists until one is exhausted
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # Move the tail pointer forward
            
        # Append the remaining nodes of the non-empty list
        tail.next = list1 if list1 else list2
        
        # Return the actual head of the merged list
        return dummy.next

        