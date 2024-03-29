class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
            cur = cur.next
        return head
