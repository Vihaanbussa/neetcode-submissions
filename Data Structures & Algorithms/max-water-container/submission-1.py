class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0;
        p2 = len(heights) - 1
        largestsum = self.findArea(p1, p2, heights)
        lastsum = 0;
        while p1 < p2:
            currsum = self.findArea(p1, p2, heights)
            if currsum > largestsum:
                largestsum = currsum
                print("p1: " + str(p1))
                print("p2: " + str(p2))
            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
            lastsum = currsum;
        return largestsum;

    def findArea(self, h1index, h2index, heights) -> int:
        h1 = heights[h1index]
        h2 = heights[h2index]
        return min(h1,h2) * (h2index-h1index)
            
            