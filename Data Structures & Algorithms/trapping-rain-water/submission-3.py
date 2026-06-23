class Solution:
    def trap(self, height: List[int]) -> int:
        maxR, r = height[len(height) -1], len(height) -1
        maxL, l = height[0], 0
        res = 0

        while l<r:
            if maxL <= maxR:
                l+=1
                if maxL - height[l] >= 0:
                    res+= maxL - height[l]
                maxL = max(height[l], maxL) 
            else:
                r-=1
                if maxR - height[r] >= 0:
                    res+= maxR - height[r]
                maxR = max(height[r], maxR)
        return res   