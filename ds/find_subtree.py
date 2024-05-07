class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        #define subtree
        subtree = defaultdict(list)
        #create sub function for inorder
        def dfs(node):
            if not node:
                return "null"
            #create a string for preorder and check with subtree dict
            s = ",".join([str(node.val), dfs(node.left), dfs(node.right)])
            if len(subtree[s]) == 1:
                res.append(node)
            #otherwise add to dict
            subtree[s].append(node)
            return s
        res = []
        dfs(root)
        return res
