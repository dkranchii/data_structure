class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])
        while q:
            rightside = None
            qlen = len(q)

            for i in range(qlen):
                node = q.popleft()
                if node:
                    rightside = node
                    q.append(node.left)
                    q.append(node.right)

            if rightside:
                res.append(rightside.val)
        return res
