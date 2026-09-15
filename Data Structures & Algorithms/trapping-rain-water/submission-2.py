class Solution:
    def trap(self, height: List[int]) -> int:
        vol = 0
        floor = 0
        stack = []
        for i in range(len(height)):
            if len(stack)==0:
                stack.append([i, height[i]])
                floor = max(height[i], floor)
                continue
            else:
                while(len(stack)>0 and height[i]>=stack[-1][1]):
                    last = stack.pop()
                    vol+= (i - last[0] - 1) * (last[1] - floor)
                    floor = last[1]
                if(len(stack)>0 and height[i]<stack[-1][1]):
                    vol+= (i - stack[-1][0] - 1) * (height[i] - floor)
                stack.append([i, height[i]])
                floor = height[i]
        return vol