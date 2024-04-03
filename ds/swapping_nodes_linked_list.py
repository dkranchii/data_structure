class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        for i in range(k - 1):
            cur = cur.next
        #define the left base on cur
        left = cur
        right = head
        while cur.next:
            cur = cur.next
            right = right.next
        left.val, right.val = right.val, left.val
        return head
