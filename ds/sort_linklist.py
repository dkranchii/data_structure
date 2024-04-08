class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # split the list into two halves
        mid = self.getMid(head)
        left = head
        right = mid.next
        mid.next = None
        # recursively sort both halves
        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)
        # merge the sorted halves
        return self.merge(left_sorted, right_sorted)

    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        # if either list is not empty, append the remaining elements
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next
