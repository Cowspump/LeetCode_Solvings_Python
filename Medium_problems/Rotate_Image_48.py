class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i]= matrix[j][i],matrix[i][j]



        for i in matrix:
            i.reverse()

s = Solution()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

s.rotate(matrix)

for i in range(len(matrix)):
    print(matrix[i])
