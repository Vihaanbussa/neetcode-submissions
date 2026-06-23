class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        prefixmax = [0] * len(height)
        suffixmax = [0] * len(height)

        if len(height) < 3:
            return 0
        
        prefixmax[0] = height[0]
        for l in range(1, len(height)):
            prefixmax[l] = max(height[l], prefixmax[l-1])
        
        suffixmax[len(height)-1] = height[len(height)-1]
        for r in range(len(height) -2, -1,-1):
            suffixmax[r] = max(height[r], suffixmax[r+1])
        
        res = 0
        for h in range(len(prefixmax)):
            res+=min(prefixmax[h], suffixmax[h]) - height[h]
        
        print(prefixmax)
        print(suffixmax)
        return res