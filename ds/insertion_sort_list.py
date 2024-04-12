class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = head, head.next
        #verify the current value with next
        while cur:
            if cur.val >= prev.val:
                prev = prev.next
                cur = cur.next
                continue
            #save the pointer of head
            temp = dummy
            while cur.val > temp.next.val:
                temp = temp.next
            prev.next = cur.next
            cur.next = temp.next
            temp.next = cur
            cur = prev.next

        return dummy.next
