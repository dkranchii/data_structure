class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr and curr.next:
            #save pntrs
            nextPair = curr.next.next
            second = curr.next
            #reverse the pair
            second.next = curr
            curr.next = nextPair
            prev.next = second
            #update pntr
            prev = curr
            curr = nextPair
        return dummy.next
