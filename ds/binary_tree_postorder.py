class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #create stack and visited 
        stack =[root]
        visited = [False]
        res = []
        while stack:
            #get the element and visited parameter
            cur, v = stack.pop(), visited.pop()
            if cur:
                #check if it was visited then add to result
                if v:
                    res.append(cur.val)
                #if not visited
                else:
                    stack.append(cur)
                    visited.append(True)
                    stack.append(cur.right)
                    visited.append(False)
                    stack.append(cur.left)
                    visited.append(False)
        return res
