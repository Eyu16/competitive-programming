class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows_will_be = len(matrix[0])
        columns_will_be = len(matrix)
        transpose = [[] for i in range(rows_will_be)]

        for i in range(columns_will_be):
            for j in range(rows_will_be):
                transpose[j].append(matrix[i][j])

        return transpose
        