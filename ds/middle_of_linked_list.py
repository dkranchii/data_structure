class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #create slow and fast pointer and return slow pointer 
        #which will indicate the middle 

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
