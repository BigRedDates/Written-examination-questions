#给定一个 n × n 的二维矩阵表示一个图像。

#将图像顺时针旋转 90 度。
#方法1：先将矩阵取转置，再关于最中间一列取对称
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        tem=0
        n=len(matrix[0])
        for i in range(n-1):
            for j in range(i+1,n):
                tem=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=tem
        for i in range(n):
            for j in range(int(n/2)):
                tem=matrix[i][j]
                matrix[i][j]=matrix[i][n-1-j]
                matrix[i][n-1-j]=tem
        print(matrix)
matrix=[[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate(matrix)

#方法二
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(m):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
        
