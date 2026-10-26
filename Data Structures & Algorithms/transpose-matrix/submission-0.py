class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        print(res)
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                res[i][j] = matrix[j][i]

        return res