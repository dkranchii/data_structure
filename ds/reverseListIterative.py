#Reverse Linked List
#Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #define a prev node as None
        prev = None
        #create a new reference which point to head
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        return prev




#Time complexity : O(n)
#Assume that nnn is the list's length, the time complexity is O(n)

#Space complexity : O(1)
