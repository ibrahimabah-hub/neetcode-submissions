class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_area = 0
        stack = []
        for i in range(len(heights)):
            index = i
            stack.append([index, heights[i]])
            while len(stack)>1 and stack[-2][1]>stack[-1][1]:
                area = (stack[-1][0] - stack[-2][0])*stack[-2][1]
                index = stack[-2][0]
                stack.pop(-2)
                largest_area = max(largest_area, area)
            stack[-1][0] = index
        width = len(heights)
        while stack:       
            area = (width-stack[-1][0])*stack[-1][1]
            largest_area = max(area, largest_area)
            stack.pop()
        return largest_area
