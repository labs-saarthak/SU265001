'''
48. Rotate Image
1886. Determine Whether Matrix Can Be Obtained By Rotation
'''
from typing import List
def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    #Transpose matrix
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))

def findRotation(mat: List[List[int]], target: List[List[int]]) -> bool:
    n = len(mat)
    for _ in range(4):
        if mat == target:
            return True
        #Transpose
        for i in range(n):
            for j in range(i+1,n):
                mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
        for row in mat:
            row.reverse()
    return False
mat = [[0,1],[1,0]]
target = [[1,0],[0,1]]
print(findRotation(mat,target))