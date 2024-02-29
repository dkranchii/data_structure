class Solution:
    def findMin(self, nums: List[int]) -> int:
        #define res with first number of the given array
        res = nums[0]
        l, r = 0 , len(nums) - 1
        # inititate lookup between left and right 
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            #find the mid value
            m = (l + r ) // 2
            res = min(res, nums[m])
            # check if mid number is greater or equal to left
            # assing left to mid + 1
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                #assing right to mid -1
                r = m -1
        return res
