import heapq

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        dummy = ListNode(0)
        curr = dummy
        heap = []
        
        # Step 1: Push the head node of each linked list into the heap
        for i, l in enumerate(lists):
            if l:
                # Store tuple as: (node_value, unique_index, node_object)
                heapq.heappush(heap, (l.val, i, l))
                
        # Step 2: Pop the minimum, link it, and advance that specific list
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next

        