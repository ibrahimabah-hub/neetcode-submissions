class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights)-1
        while(l<r):
            if heights[l]<heights[r]:
                area = heights[l]*(r-l)
                l+=1
            else:
                area = heights[r]*(r-l)
                r-=1
            if area>max_area:
                max_area = area
        return max_area
        
