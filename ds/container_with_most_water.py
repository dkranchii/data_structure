class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        #define left and right pointers
        l,r= 0, len(height) -1
        #iterate for specified condition of two pointers and return the results
        while l < r:
            area =  (r - l) * min(height[l],height[r])
            res = max(res, area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
