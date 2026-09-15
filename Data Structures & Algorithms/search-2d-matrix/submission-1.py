class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])
        if matrix[0][0]== target:
            return True
        while(top<bottom-1):
            y = (top+bottom)//2
            idx = matrix[y][0]
            if idx == target:
                return True
            if idx> target:
                bottom = y
            else:
                if matrix[y][-1]>target:
                    break
                top = y
        while(left < right-1):
            x = (left + right)//2
            y = (top + bottom)//2
            idx = matrix[y][x]
            if idx == target:
                return True
            if idx < target:
                left = x
            else:
                right = x
        return False

