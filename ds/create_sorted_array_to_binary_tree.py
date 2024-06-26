class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #write a helper function
        def helper(l, r):
            if l > r:
                return None
            mid = (l + r ) // 2
            root = TreeNode(nums[mid])
            root.left = helper(l, mid-1)
            root.right = helper(mid + 1, r)
            return root
        #return the helper function

        return helper(0, len(nums) - 1)
