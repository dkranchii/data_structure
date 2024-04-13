class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, cur = 0, head
        #find the length
        while cur:
            cur = cur.next
            length += 1

        base_len , remainder = length // k , length % k
        #start from beginning
        cur = head
        #define list to save the result
        res = []
        for i in range(k):
            res.append(cur)
            for j in range(base_len - 1 + ( 1 if remainder else 0)):
                if not cur: 
                    break
                cur = cur.next
            remainder = remainder - ( 1 if remainder else 0)
            #add none to end of each partition
            if cur:
                next_node = cur.next
                cur.next = None
                cur = next_node
        return res
