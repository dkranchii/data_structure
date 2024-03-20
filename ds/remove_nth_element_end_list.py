def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize two pointers, left and right
        left = dummy
        right = dummy
        
        # Move right pointer n steps ahead
        for _ in range(n):
            right = right.next
        
        # Move both pointers until right reaches the end
        while right.next:
            left = left.next
            right = right.next
        
        # Remove the nth node from the end
        left.next = left.next.next
        
        return dummy.next
