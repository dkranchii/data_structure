class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iterative solution 
        #define these two variable which can help us to navigate
        prev, curr = None, head
        while curr:
            #nxt variable will keep the pointer for next element
            nxt = curr.next
            #by doing curr.next equal to prev will redirect the pointer to Null
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
