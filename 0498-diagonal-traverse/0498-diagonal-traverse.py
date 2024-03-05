class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        order = list()
        numberOfRows = len(matrix)
        numberOfColumns = len(matrix[0])
        counter = 0
        numberOfDiagonals = numberOfRows + numberOfColumns - 1
        while counter < (numberOfDiagonals):
            if counter % 2 == 1:
                if counter < numberOfColumns:
                    j = counter
                    i = 0
                else:
                    j = numberOfColumns - 1
                    i = counter - numberOfColumns + 1
                while i < numberOfRows and j >= 0:
                    order.append(matrix[i][j])
                    j -= 1
                    i += 1
            else:
                if counter < numberOfRows:
                    i = counter
                    j = 0
                else:
                    j = counter - numberOfRows + 1
                    i = numberOfRows - 1
                while j < numberOfColumns and i >= 0:
                    order.append(matrix[i][j])
                    j += 1
                    i -= 1
            counter += 1
        return order