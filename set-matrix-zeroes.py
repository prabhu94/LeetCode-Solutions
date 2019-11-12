#https://leetcode.com/problems/set-matrix-zeroes/
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    
                    # change the row and column to zeroes
                    for r in range(len(matrix)):
                        if matrix[r][j] !=0:
                            matrix[r][j] = 'pholder'
                    for c in range(len(matrix[i])):
                        if matrix[i][c] !=0:
                            matrix[i][c] = 'pholder'
                            
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 'pholder':
                    matrix[i][j] = 0
        
