#867. Transpose Matrix
from typing import List
def transpose(matrix: List[List[int]]) -> List[List[int]]:
    rows,cols = len(matrix),len(matrix[0])
    res = [[0]*rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            res[j][i] = matrix[i][j]
    return res
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))

#566. Reshape the Matrix
